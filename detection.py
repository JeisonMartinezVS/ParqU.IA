# detection.py

import cv2
import pytesseract

# Configura la ruta al ejecutable de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jeison Martinez\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def detectar_placa(imagen_ruta):
    try:
        img = cv2.imread(imagen_ruta)
        if img is None:
            return None
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img,(3,3))
        img = cv2.Canny(img,150,200)
        img = cv2.dilate(img,None,iterations=1)
        cnts,_ = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, cnts, -1, (0,255,0),2)
        
        for c in cnts:
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            epsilon = 0.09*cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, epsilon, True)
            if len(approx)==4 and area > 9000:
                cv2.drawContours(img,[c],0,(0,255,0),2)
        texto = pytesseract.image_to_string(img, config='--psm 8')
        placa = ''.join(filter(str.isalnum, texto)).upper()
        return placa if placa else None
    except Exception as e:
        print(f"Error al detectar la placa: {e}")
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
        placa = detectar_placa(cv2.imread(imagen_ruta))
        if placa:
            print(f"Placa detectada: {placa}")
        else:
            print("No se pudo detectar ninguna placa.")