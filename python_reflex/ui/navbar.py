import reflex as rx
from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar_user() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/calendar-date-icon.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Expire", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", navigation.routes.HOME_ROUTE),
                    navbar_link("Categoría", navigation.routes.CATEGORY_ROUTE),
                    navbar_link("Elemento", navigation.routes.ELEMENT_ROUTE),
                    navbar_link("Calendario", navigation.routes.CALENDAR_ROUTE),
                    navbar_link("Notificación", navigation.routes.NOTIFICATION_ROUTE),
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("user"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Perfil"),
                        #rx.menu.separator(),
                        rx.menu.item("Salir"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/calendar-date-icon.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Expire", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.icon("align-justify"),
                            size="2",
                            radius="full",
                        )
                    ),
                    rx.menu.content(
                        rx.menu.item("Inicio",
                            on_click=navigation.NavState.to_home),
                        rx.menu.item("Categoria",
                            on_click=navigation.NavState.to_category),
                        rx.menu.item("Elemento",
                            on_click=navigation.NavState.to_element),
                        rx.menu.item("Calendario",
                            on_click=navigation.NavState.to_calendar),
                        rx.menu.item("Notificación",
                            on_click=navigation.NavState.to_notification),
                        rx.menu.separator(),
                        rx.menu.item("Perfil"),
                        rx.menu.item("Salir"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )
