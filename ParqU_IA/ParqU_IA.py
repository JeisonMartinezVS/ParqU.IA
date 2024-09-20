import reflex as rx
import cv2
import pytesseract
import os

from ParqU_IA.views.navbar import navbar
from ParqU_IA.views.footer import footer
from ParqU_IA.views.datatable import datatable

from rxconfig import config

class State(rx.State):
    """The app state."""
    
    imagen_capturada: str = None

# Método para inicializar la cámara y capturar cuadros continuamente
def procesar_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            # Convertir la imagen a escala de grises y aplicar OCR para detectar texto
            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            texto = pytesseract.image_to_string(gris, config='--psm 8')
            placa_detectada = ''.join(filter(str.isalnum, texto)).upper()

            # Verificar si es una placa válida (6 caracteres)
            if len(placa_detectada) == 6:
                print(f"Placa detectada: {placa_detectada}")
                # Guardar la imagen automáticamente
                ruta_imagen = os.path.join(os.getcwd(), "placa_capturada.jpg")
                cv2.imwrite(ruta_imagen, frame)
                State.imagen_capturada = ruta_imagen
                cap.release()
                break
        else:
            break

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                rx.container(
                    rx.image(
                        src="/TarifasU.jpg",
                        alt="Camara No Iniciada",
                        class_name="w-full h-full"
                    ),
                ),
                rx.button(
                    "Capturar placa",
                    class_name="cursor-pointer"
                ),
                class_name="bg-[#1F2937] m-6 items-center justify-center pb-3"    
            ),
        ),
        rx.box(
            datatable()    
        ),
        rx.el.footer(
          footer(),
          class_name="w-full inset-x-0 bottom-0"
        ),
        class_name="bg-[#111827]"
    ),

# Ejecutar la captura automática al iniciar la aplicación
def run():
    # Iniciar la captura automática de placas
    procesar_video()

app = rx.App()
app.add_page(index)
app._compile()
