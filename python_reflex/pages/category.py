import reflex as rx
from ..ui.navbar import navbar_user
from .. import navigation

from ..components import category_table


@rx.page(route=navigation.routes.CATEGORY_ROUTE)
def category_page() -> rx.Component:
    return rx.fragment(
        navbar_user(),
        rx.vstack(
            rx.box(
                width="75%", 
                border_radius="20px"),
            rx.box(
                category_table.main_table(),
                width="75%",
            ),
            width="100%",
            justify="center",
            align="center",
            spacing="6",
        ), 
        rx.color_mode.button(position="bottom-left"),
    )