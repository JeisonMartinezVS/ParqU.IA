# Sistema de Captura y Detección de Placas Vehiculares

Este proyecto es una aplicación que captura imágenes desde una cámara, detecta placas vehiculares en las imágenes, y determina el tipo de vehículo (carro o moto) basado en el formato de la placa.

## Características

- **Captura de Imagen:** Utiliza la cámara conectada al sistema para capturar imágenes.
- **Detección de Placa:** Extrae el texto de la placa vehicular de la imagen utilizando OCR (Tesseract).
- **Validación de Placa:**
  - Asegura que las placas detectadas tengan exactamente 6 caracteres alfanuméricos.
  - Determina si la placa pertenece a un carro (termina en número) o a una moto (termina en letra).
- **Cálculo de Precio:** Calcula el precio según el tipo de vehículo y el rol del usuario (e.g., visitante).

## Requisitos

- **Python 3.7+**
- **OpenCV** (`cv2`)
- **Tesseract-OCR**
- **Pytesseract**
- **Tkinter** (para la interfaz gráfica)

## Instalación

1. **Dependencias**

```
pip install mysql-connector-python opencv-python pytesseract pillow
```
