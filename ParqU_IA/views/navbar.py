import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/LogoParq.png",
                        class_name="w-[120px] h-auto roundend-[25%]"
                    ),
                    rx.grid(
                        rx.heading(
                            "ParqU.IA",
                            class_name="size-7"
                        ),
                            rx.text(
                            "Gestor de placas inteligente"
                        ),    
                    ),
                    class_name="items-center bg-[#1F2937] w-full text-white"
                ),
            ),
        ),
    )