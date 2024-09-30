import reflex as rx

def button(icon: str, text: str) -> rx.Component:
    return rx.button(
        rx.icon(icon),
        text,
        class_name="cursor-pointer"
    )