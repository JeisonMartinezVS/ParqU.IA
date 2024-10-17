import reflex as rx
from datetime import datetime, timezone


class MomentState(rx.State):
    date_now: datetime = datetime.now(timezone.utc)

    def update(self):
        self.date_now = datetime.now(timezone.utc)

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
                            "Gestion del parqueadero UNIMINUTO"
                        ),    
                    ),
                    rx.box(
                        rx.grid(
                            rx.moment(
                                MomentState.date_now,
                                format="YYYY-MM-DD"
                            ),
                            rx.moment(
                                interval=1000, 
                                format="HH:mm:ss"
                            ),
                        ),
                        class_name="text-[15px] ml-[700px]"    
                    ),
                    class_name="items-center bg-[#1F2937] w-full text-white"
                ),
            ),
        ),
    )