# detection.py

import cv2
import pytesseract
import re

# Configura la ruta al ejecutable de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jeison Martinez\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def preprocesar_imagen(img):
    """
    Realiza un preprocesamiento en la imagen para mejorar la detección de la placa.
    """
    # Convertir a escala de grises
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aumentar el contraste
    img_contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)

    # Aplicar filtro de desenfoque para reducir ruido
    img_blur = cv2.GaussianBlur(img_contrast, (5, 5), 0)
    
    # Binarización adaptativa para mejorar la visibilidad de caracteres
    img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY, 11, 2)
    return img_thresh

def detectar_placa(imagen_ruta):
    try:
        img = cv2.imread(imagen_ruta)
        if img is None:
            return None
        
        # Preprocesamiento de la imagen
        img_thresh = preprocesar_imagen(img)
        
        # Detectar contornos
        cnts, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts:
            area = cv2.contourArea(c)
            x, y, w, h = cv2.boundingRect(c)
            epsilon = 0.09 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            
            # Buscar contornos con forma rectangular y área significativa
            if len(approx) == 4 and area > 9000:
                # Extraer la región de interés (ROI) de la placa
                roi = img_thresh[y:y + h, x:x + w]
                
                # Ajuste de configuración de Tesseract para mejorar precisión en placas
                config_tesseract = '--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                
                # Extraer texto con OCR
                texto = pytesseract.image_to_string(roi, config=config_tesseract)
                
                # Limpiar el texto y validar el formato de la placa
                placa = ''.join(filter(str.isalnum, texto)).upper()
                if placa:
                    return placa
        return None
    except Exception as e:
        print(f"Error al detectar la placa: {e}")
        return None

def validar_placa(placa):
    """
    Valida si la placa corresponde a un carro o una moto basándose en el formato:
    - Carro: Tres letras + tres números (ABC123).
    - Moto: Tres letras + dos números + una letra (ABC12D).
    """
    # Expresiones regulares para validar placas de carro y moto
    carro_pattern = r"^[A-Z]{3}[0-9]{3}$"
    moto_pattern = r"^[A-Z]{3}[0-9]{2}[A-Z]$"
    
    if re.match(carro_pattern, placa):
        return "carro"
    elif re.match(moto_pattern, placa):
        return "moto"
    else:
        return None

def calcular_precio(tipo_vehiculo, rol):
    precios_base = {
        'carro': 5200,
        'moto': 3600
    }
    descuentos = {
        'estudiante': 900,  # 20% de descuento
        'visitante': 0.0    # Sin descuento
    }
    
    precio_base = precios_base.get(tipo_vehiculo.lower())
    descuento = descuentos.get(rol.lower())
    
    if precio_base is not None and descuento is not None:
        precio_final = precio_base - descuento
        return precio_final
    else:
        return None

def capturar_imagen_camara():
    # Abre la cámara
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        # Muestra la imagen capturada
        cv2.imshow('Captura de Placa', frame)

        # Espera a que el usuario presione la tecla 's' para guardar la imagen
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    # Guarda la imagen capturada
    imagen_ruta = 'captura_placa.jpg'
    cv2.imwrite(imagen_ruta, frame)
    cap.release()
    cv2.destroyAllWindows()

    return imagen_ruta

if __name__ == "__main__":
    # Captura la imagen de la placa
    imagen_ruta = capturar_imagen_camara()
    
    if imagen_ruta:
        # Detecta la placa
        placa = detectar_placa(imagen_ruta)
        
        if placa:
            print(f"Placa detectada: {placa}")
            
            # Valida si es carro o moto
            tipo_vehiculo = validar_placa(placa)
            if tipo_vehiculo == "carro":
                print("La placa pertenece a un carro.")
            elif tipo_vehiculo == "moto":
                print("La placa pertenece a una moto.")
            else:
                print("Formato de placa no reconocido.")
            
            # Solicitar rol del usuario y calcular precio
            rol = input("Por favor ingrese su rol (estudiante o visitante): ").lower()
            precio = calcular_precio(tipo_vehiculo, rol)
            if precio is not None:
                print(f"El precio para el {tipo_vehiculo} con rol {rol} es: {precio}")
            else:
                print("No se pudo calcular el precio.")
        else:
            print("No se pudo detectar ninguna placa.")
