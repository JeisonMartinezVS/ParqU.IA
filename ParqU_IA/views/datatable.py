import reflex as  rx

def datatable() -> rx.Component:
    return rx.box(
        rx.hstack(
                    rx.text(
                        "Vehiculos Registrados",
                        class_name="font-bold size-2"
                    ),
                    rx.button(
                        "+ Registro Manual",
                        class_name="bg-lime-600 top-0 start-0"    
                    ),
                class_name="p-6"
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Placa"),
                        rx.table.column_header_cell("Tipo"),
                        rx.table.column_header_cell("Nombre"),
                        rx.table.column_header_cell("Hora"),
                        rx.table.column_header_cell("Estado"),
                    ),
                ),
            rx.table.body(
                rx.table.row(
                    rx.table.row_header_cell("ABC123"),
                    rx.table.cell("Automóvil"),
                    rx.table.cell("Juan Pérez"),
                    rx.table.cell("14:30"),
                    rx.table.cell("Autorizado"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("XYZ789"),
                    rx.table.cell("Motocicleta"),
                    rx.table.cell("Lucía Rodríguez"),
                    rx.table.cell("15:45"),
                    rx.table.cell("Pendiente"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("LMN456"),
                    rx.table.cell("Camioneta"),
                    rx.table.cell("Pedro Morales"),
                    rx.table.cell("16:00"),
                    rx.table.cell("Denegado"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("DEF321"),
                    rx.table.cell("Automóvil"),
                    rx.table.cell("Carlos García"),
                    rx.table.cell("17:10"),
                    rx.table.cell("Autorizado"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("HIJ654"),
                    rx.table.cell("Motocicleta"),
                    rx.table.cell("Ana Torres"),
                    rx.table.cell("17:30"),
                    rx.table.cell("Pendiente"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("GHI987"),
                    rx.table.cell("Camión"),
                    rx.table.cell("María López"),
                    rx.table.cell("18:00"),
                    rx.table.cell("Autorizado"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("KLM321"),
                    rx.table.cell("SUV"),
                    rx.table.cell("Fernando Díaz"),
                    rx.table.cell("18:45"),
                    rx.table.cell("Denegado"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("NOP876"),
                    rx.table.cell("Automóvil"),
                    rx.table.cell("Isabel Ortiz"),
                    rx.table.cell("19:00"),
                    rx.table.cell("Pendiente"),
                ),
                rx.table.row(
                    rx.table.row_header_cell("QRS543"),
                    rx.table.cell("Camioneta"),
                    rx.table.cell("Sergio Álvarez"),
                    rx.table.cell("19:15"),
                    rx.table.cell("Autorizado"),
                )
            ),
            width="100%",
        ),
            class_name="bg-[#1F2937] m-6 items-center justify-center"    
    )