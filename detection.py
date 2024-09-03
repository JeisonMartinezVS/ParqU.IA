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
        texto = pytesseract.image_to_string(img, config='--psm 8')
        placa = ''.join(filter(str.isalnum, texto)).upper()
        return placa if placa else None
    except Exception as e:
        print(f"Error al detectar la placa: {e}")
        return None

def calcular_precio(tipo_vehiculo, rol):
    precios_base = {
        'carro': 1000,
        'moto': 500
    }
    descuentos = {
        'estudiante': 0.2,  # 20% de descuento
        'visitante': 0.0    # Sin descuento
    }
    
    precio_base = precios_base.get(tipo_vehiculo.lower())
    descuento = descuentos.get(rol.lower())
    
    if precio_base is not None and descuento is not None:
        precio_final = precio_base * (1 - descuento)
        return precio_final
    else:
        return None
