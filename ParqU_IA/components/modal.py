import reflex as rx
import re
from ParqU_IA.database.db import registrar_placas


class SelectVehicule(rx.State):
    tipo_vehiculo: str = "Moto"
    placa: str = ""
    mensaje_error: str = ""
    
    def validar_placa(self):
        if self.tipo_vehiculo == "Moto":
            pattern = r'^[A-Z]{3}[0-9]{2}[A-Z]$'
        elif self.tipo_vehiculo == "Carro":
            pattern = r'^[A-Z]{3}[0-9]{3}$'
        else:
            pattern: None
            
        if pattern and re.match(pattern, self.placa):
            self.mensaje_error = ""
        else:
            self.mensaje_error = "La placa ingresada no corresponde a una placa de " + self.tipo_vehiculo
            
    def on_placa_change(self, value):
        self.placa = value.upper()
        self.validar_placa()
        
    def set_tipo_vehiculo(self, value):
        self.tipo_vehiculo = value
        self.validar_placa()

class State(rx.State):
    nombre: str = ""
    placa: str = ""
    tipo_vehiculo: str = ""
    rol: str = ""
    mensaje: str = ""
    
    def registrar(self):
        if self.placa == "":
            self.mensaje = "El campo placa esta vacio"
        else:
            result = registrar_placas(self.nombre, self.placa, self.tipo_vehiculo, self.rol)
            self.mensaje = result
        
    def set_nombre(self, value):
        self.nombre = value
        
    def set_rol(self, value):
        self.rol = value

    def set_tipo_vehiculo(self, value):
        self.tipo_vehiculo = value
        SelectVehicule.set_tipo_vehiculo(value)

    def set_placa(self, value):
        self.placa = value
        SelectVehicule.on_placa_change(value)

def modal() -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("user-round-plus"),
                        "Registrar Usuario",
                        class_name="bg-lime-600 top-0 start-0 cursor-pointer",          
                    ),
                ),
                    rx.dialog.content(
                        rx.dialog.title("Agregar nuevo usuario"),
                        rx.flex(
                            rx.vstack(
                                rx.flex(
                                    rx.text(
                                        "Nombre (Estudiante): ",
                                        class_name="mr-2"
                                        ),
                                    rx.input(
                                        placeholder="Ingresar el nombre",
                                        name="nombre",
                                        class_name="w-auto",
                                        on_change=lambda value: State.set_nombre(value),
                                        required=True
                                        ),
                                    class_name="items-center"
                                    ),
                                rx.flex(
                                    rx.text(
                                        "Rol: ",
                                        class_name="mr-2"
                                        ),
                                    rx.select(
                                        ["Estudiante", "Visitante"],
                                        placeholder="Seleccione el rol",
                                        label="Elija el rol",
                                        on_change=lambda value: State.set_rol(value),
                                        required=True
                                        ),    
                                    class_name="items-center"
                                    ),
                                rx.flex(
                                    rx.text(
                                        "Vehiculo: ",
                                        class_name="mr-2"
                                        ),
                                    rx.select(
                                        ["Moto", "Carro"],
                                        # value=SelectVehicule.tipo_vehiculo,
                                        on_change=lambda value: State.set_tipo_vehiculo(value),
                                        placeholder="Tipo de vehiculo",
                                        label="Elija el vehiculo",
                                        required=True
                                        ),
                                    class_name="items-center"
                                    ),
                                rx.flex(
                                    rx.text(
                                        "Placa Vehicular: ",
                                        class_name="mr-2"
                                        ),
                                    rx.input(
                                        value=SelectVehicule.placa,
                                        on_change=lambda value: State.set_placa(value),
                                        max_length=6,
                                        min_length=5,
                                        placeholder="Ingrese la placa",
                                        name="placa",
                                        id="placa",
                                        class_name="uppercase",
                                        required=True
                                        ),
                                    class_name="items-center"
                                    ),
                                rx.text(SelectVehicule.mensaje_error, style={"color": "red"}), # Mostrar mensaje de error
                                class_name="w-full justify-center"
                            ),
                        ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Salir", class_name="bg-red-800"),
                        ),
                        rx.button(
                            "Guardar", 
                            class_name="bg-green-500",
                            on_click=State.registrar
                            ),
                        spacing="3",
                        class_name="pt-8"
                    ),
                    rx.box(
                            rx.badge(State.mensaje, variant="outline")
                    )
                ),
            )