import reflex as rx
from ..ui.navbar import navbar_user
from .. import navigation

@rx.page(route=navigation.routes.HOME_ROUTE)
def home_page() -> rx.Component:
    #return rx.container(
    return rx.fragment(
        navbar_user(),
        rx.box(
            rx.vstack(
                rx.heading("Expire", size="9"),
                rx.text(
                    "Bienvenido",
                    align="right",
                    size="5",
                ),
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
