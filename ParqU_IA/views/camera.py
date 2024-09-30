import reflex as rx
import requests

def camera() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='http://localhost:5000/video_feed',  # Cambia la URL al endpoint del servidor Flask
            alt="Flujo de video de la cámara",
            class_name="w-[10%] h-auto"  # Ajusta el tamaño según sea necesario
        ),
        rx.hstack(
            rx.button(
                rx.icon("camera"),
                "Activar Cámara",
                # on_click=lambda: requests.get('http://localhost:5000/video_feed')
            ),
            rx.button(
                "plus",
                "Capturar placa"
            )
        ),
        class_name="bg-[#1F2937] m-6 items-center justify-center pb-3"
    )
