# Sistema de Captura y Detección de Placas Vehiculares

Este proyecto es una aplicación que captura imágenes desde una cámara, detecta placas vehiculares en las imágenes, y determina el tipo de vehículo (carro o moto) basado en el formato de la placa. Esto estaria basado en el manejo del estacionamiento en la universidad **Uniminuto**

![Texto Alternativo](TarifasU.jpg)

## Características

- **Captura de Imagen:** Utiliza la cámara conectada al sistema para capturar imágenes.
- **Detección de Placa:** Extrae el texto de la placa vehicular de la imagen utilizando OCR (Tesseract).
- **Validación de Placa:**
  - Asegura que las placas detectadas tengan exactamente 6 caracteres alfanuméricos.
  - Determina si la placa pertenece a un carro (termina en número) o a una moto (termina en letra).
- **Cálculo de Precio:** Calcula el precio según:
  - **Tipo de Vehículo:** Los carros y motos tienen diferentes tarifas.
  - **Rol del Usuario:** Los usuarios pueden tener roles como **estudiantes**, **profesores** o **visitantes**, que influyen en el precio a pagar.

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
