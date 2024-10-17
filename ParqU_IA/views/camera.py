import reflex as rx
import requests

from ParqU_IA.components.upload import upload

class CameraState(rx.State):
    camera_active: bool = False
    placa_detectada: str = ""
    tipo_vehiculo: str = ""
    mensaje: str = ""

    def toggle_camera(self):
        self.camera_active = not self.camera_active

    def capturar_placa(self, nombre: str, rol: str):
        try:
            response = requests.post(
                'http://localhost:5000/capturar_placa',
                json={'nombre': nombre, 'rol': rol}
            )
            if response.status_code == 200:
                data = response.json()
                self.placa_detectada = data.get('placa', '')
                self.tipo_vehiculo = data.get('tipo_vehiculo', '')
                self.mensaje = data.get('mensaje', '')
            else:
                self.mensaje = "Error al capturar la placa"
        except Exception as e:
            self.mensaje = f"Error: {str(e)}"

    def cargar_imagen(self, imagen_path: str):
        try:
            with open(imagen_path, 'rb') as img_file:
                files = {'imagen': img_file}
                response = requests.post('http://localhost:5000/cargar_imagen', files=files)
                
                if response.status_code == 200:
                    data = response.json()
                    self.placa_detectada = data.get('placa', '')
                    self.tipo_vehiculo = data.get('tipo_vehiculo', '')
                    self.mensaje = data.get('mensaje', '')
                else:
                    self.mensaje = "Error al cargar la imagen"
        except Exception as e:
            self.mensaje = f"Error: {str(e)}"

def camera() -> rx.Component:
    return rx.vstack(
        rx.cond(
            CameraState.camera_active,
            rx.image(
                src='http://localhost:5000/video_feed',
                alt="Flujo de video de la cámara",
                class_name="w-[70%] h-[500px] mt-5"
            ),
            rx.image(
                src='CamaraNoActivada.png',
                alt="Cámara apagada",
                class_name="w-[70%] h-[500px] mt-5"
            )
        ),
        rx.hstack(
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
            rx.button(
                "Capturar Placa",
                on_click=lambda: CameraState.capturar_placa("Usuario", "Admin"),
                class_name="bg-green-500 text-white px-4 py-2 rounded"
            ),
            upload()
        ),
        rx.text(f"Placa: {CameraState.placa_detectada}", class_name="text-white mt-5"),
        rx.text(f"Tipo de Vehículo: {CameraState.tipo_vehiculo}", class_name="text-white mt-1"),
        rx.text(f"Mensaje: {CameraState.mensaje}", class_name="text-white mt-1"),
        class_name="bg-[#1F2937] m-6 items-center justify-center pb-8",
    )

