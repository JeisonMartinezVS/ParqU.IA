import reflex as rx

def upload() -> rx.Component:
    return rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        rx.icon("image"),
                        "Imagen",
                        class_name="bg-lime-600 top-0 start-0 cursor-pointer",          
                    ),
                ),
                    rx.dialog.content(
                        rx.dialog.title("Agregar nuevo usuario"),
                        rx.upload(
                            rx.text(
                                    "Drag and drop files here or click to select files"
                                ),
                            id="my_upload",
                            border="1px dotted rgb(107,99,246)",
                            padding="5em",
                            )
                ),
            )