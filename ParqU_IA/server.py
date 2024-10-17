import cv2
from flask import Flask, Response, jsonify, request
import pytesseract
import re
import numpy as np

app = Flask(__name__)

# Configura la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Jeison Martinez\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Funciones de preprocesamiento y detección reutilizadas del código anterior
def preprocesar_imagen(img):
    """
    Realiza un preprocesamiento en la imagen para mejorar la detección de la placa.
    """
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_contrast = cv2.convertScaleAbs(img_gray, alpha=1.5, beta=0)
    img_blur = cv2.GaussianBlur(img_contrast, (5, 5), 0)
    img_thresh = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return img_thresh

def detectar_placa(imagen_ruta):
    img = cv2.imread(imagen_ruta)
    if img is None:
        return None, None
    
    # Preprocesamiento de la imagen
    img_thresh = preprocesar_imagen(img)
    
    # Detectar contornos
    cnts, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.09 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        
        if len(approx) == 4 and area > 9000:
            roi = img_thresh[y:y + h, x:x + w]
            
            # Ajuste de configuración de Tesseract
            config_tesseract = '--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            
            # Extraer texto con OCR
            texto = pytesseract.image_to_string(roi, config=config_tesseract)
            
            # Limpiar el texto
            placa = ''.join(filter(str.isalnum, texto)).upper()
            
            # Validar formato de placa
            if re.match(r'^[A-Z]{3}\d{3,4}[A-Z]?$', placa):
                tipo_vehiculo = 'carro' if placa[-1].isdigit() else 'moto'
                return placa, tipo_vehiculo
    
    return None, None

def generar_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generar_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capturar_placa', methods=['POST'])
def capturar_placa():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return jsonify({"error": "No se pudo acceder a la cámara."}), 500

    # Guarda la imagen capturada
    imagen_ruta = 'captura_placa.jpg'
    cv2.imwrite(imagen_ruta, frame)
    cap.release()

    # Detectar placa
    placa, tipo_vehiculo = detectar_placa(imagen_ruta)
    if placa:
        return jsonify({"placa": placa, "tipo_vehiculo": tipo_vehiculo}), 200
    else:
        return jsonify({"error": "No se pudo detectar ninguna placa."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
