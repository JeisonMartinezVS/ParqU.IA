import reflex as rx
import cv2
import pytesseract
import os

from ParqU_IA.views.camera import camera
from ParqU_IA.views.navbar import navbar
from ParqU_IA.views.footer import footer
from ParqU_IA.views.datatable import datatable

from rxconfig import config

class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            camera()
            ),
        rx.box(
            datatable(),
            class_name="h-full text-white"    
        ),
        rx.box(
            rx.el.footer(
                footer(),
                class_name="w-full inset-x-0 bottom-0"
            ),    
        ),
        class_name="bg-[#111827] text-white m-0 p-0"
    ),

app = rx.App()
app.add_page(index)
app._compile()
