import reflex as rx

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.text(
              "© 2024 ParqU.IA. Todos los derechos reservados."  
            ),
            rx.hstack(
                # Politica de privacidad
                rx.popover.root(
                  rx.popover.trigger(
                      rx.button(
                            "Politica de privacidad" 
                        ),
                  ),
                  rx.popover.content(
                      rx.flex(
                          rx.text("Politica de privacidad"),
                          rx.popover.close(
                              rx.button("Cerrar"),
                          ),
                          direction="column",
                          spacing="3",
                      ),
                  ),
                ),
                # Terminos y condiciones
                rx.popover.root(
                  rx.popover.trigger(
                      rx.button(
                            "Terminos y condiciones" 
                        ),
                  ),
                  rx.popover.content(
                      rx.flex(
                          rx.text("Terminos y condiciones"),
                          rx.popover.close(
                              rx.button("Cerrar"),
                          ),
                          direction="column",
                          spacing="3",
                      ),
                  ),
                ),
            ),
        ),
        class_name="items-center bg-[#1F2937] w-full h-full inset-x-0 bottom-0 text-white"
    )