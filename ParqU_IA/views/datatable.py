import reflex as rx
from sqlmodel import select, func
from ParqU_IA.components.modal import modal
from ParqU_IA.database.db import obtener_usuarios

class UserState(rx.State):
    users: list[dict] = []
    
    total_items: int
    offset: int = 0
    limit: int = 3
    
    def mostrar_usuarios(self):
        self.users = obtener_usuarios()


def mostrar_registro(user: dict):
    """Muestra un registro de usuario en una fila de la tabla."""
    return rx.table.row(
        rx.table.cell(user['nombre']),
        rx.table.cell(user['placa']),
        rx.table.cell(user['tipo_vehiculo']),
        rx.table.cell(user['rol']),
        class_name="text-white"
    )

# Componente para mostrar la tabla de usuarios
def datatable() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Vehículos Registrados", class_name="font-bold size-2"),
            modal(),  # Asumimos que ya tienes este modal implementado
            class_name="p-6"
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Estudiante"),
                    rx.table.column_header_cell("Placa"),
                    rx.table.column_header_cell("Tipo"),
                    rx.table.column_header_cell("Rol"),
                    class_name="text-white"
                ),
            ),
            rx.table.body(
                # Usamos rx.foreach para iterar sobre los registros de UserState
                rx.foreach(UserState.users, mostrar_registro)
            ),
        ),
        on_mount=UserState.mostrar_usuarios,  # Cargamos los datos cuando el componente se monta
        class_name="bg-[#1F2937] m-6 items-center justify-center text-white h-full"
    )