import reflex as rx
from ..ui.navbar import navbar_user
from .. import navigation

@rx.page(route=navigation.routes.CALENDAR_ROUTE)
def calendar_page() -> rx.Component:
    return rx.fragment(
        navbar_user(),
        rx.box(
            rx.vstack(
                rx.heading("Calendar", size="9"),
                rx.text(
                    "Welcome",
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
