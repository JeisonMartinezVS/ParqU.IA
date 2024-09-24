import reflex as rx
from ParqU_IA.components.modal import modal
from ParqU_IA.database.db import obtener_usuarios

class UserState(rx.State):
    users: list[dict] = []
    
    def mostrar_usuarios(self):
        self.users = obtener_usuarios()

def datatable() -> rx.Component:

    return rx.box(
        rx.hstack(
            rx.text("Vehiculos Registrados", class_name="font-bold size-2"),
            modal(),
            class_name="p-6"
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Placa"),
                    rx.table.column_header_cell("Tipo"),
                    rx.table.column_header_cell("Rol"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    UserState.users,  # Usa el estado de usuario
                    lambda user: rx.table.row(    
                        rx.table.cell(user['placa']),
                        rx.table.cell(user['tipo_vehiculo']),
                        rx.table.cell(user['rol'])
                    )
                ),
            ),
            width="100%",
            class_name="text-white"
        ),
        class_name="bg-[#1F2937] m-6 items-center justify-center text-white"    
    )
