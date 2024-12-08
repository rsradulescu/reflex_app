import reflex as rx
from rxconfig import config
from .ui.login import login_default
from . import pages, navigation

class State(rx.State):
    title = "Expire"
    sesion_init_text = "Para comenzar a utilizar la aplicación cree o inicie sesión"
    logo_src= "/calendar-date-icon.jpg"


def index() -> rx.Component:
    #return rx.container(
    return rx.fragment(
        rx.box(
            rx.vstack(
                rx.heading(State.title, size="9"),
                rx.text(
                    State.sesion_init_text,
                    align="right",
                    #rx.code(f"{config.app_name}/{config.app_name}.py"),
                    size="5",
                ),
                login_default(),

                spacing="5",
                justify="center",
                align="center",
                min_height="85vh",
            ),
            padding="1em",
            width="100%",
            justify="center",
            align="center",

        ),
        rx.color_mode.button(position="bottom-left"),
    )

#---------------
app = rx.App()
app.add_page(index)