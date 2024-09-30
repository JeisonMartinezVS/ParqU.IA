import reflex as rx

class CameraState(rx.State):
    camera_active: bool = False  # Estado para controlar si la cámara está activa o no

    def toggle_camera(self):
        """Activa o desactiva la cámara y actualiza el estado."""
        self.camera_active = not self.camera_active

def camera() -> rx.Component:
    return rx.vstack(
        # Si la cámara está activa, mostramos el flujo de video
        rx.cond(
            CameraState.camera_active,
            rx.image(
                src='http://localhost:5000/video_feed',  # URL para el flujo de video desde Flask
                alt="Flujo de video de la cámara",
                class_name="w-[50%] h-[500px] mt-5"
            ),
            # Si la cámara no está activa, mostramos una imagen estática de cámara apagada
            rx.image(
                src='CamaraNoActivada.png',  # Imagen de cámara apagada
                alt="Cámara apagada",
                class_name="w-[50%] h-[500px] mt-5"
            )
        ),
        rx.hstack(
            # Botón para activar o desactivar la cámara
            rx.button(
                rx.cond(
                    CameraState.camera_active,
                    rx.icon("camera-off"),
                    rx.icon("camera"),
                ),
                rx.cond(
                    CameraState.camera_active,
                    "Apagar Cámara",
                    "Activar Cámara"    
                ),
                on_click=CameraState.toggle_camera,
                class_name="bg-blue-500 text-white px-4 py-2 rounded"
            ),
        ),
        class_name="bg-[#1F2937] m-6 items-center justify-center pb-3"
    )
