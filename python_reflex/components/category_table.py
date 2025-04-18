import reflex as rx
from ..backend.category import State, Category
from .form_field import form_field

def show_category(category: Category):
    """Show a category in a table row."""

    return rx.table.row(
        rx.table.cell(category.name),
        rx.table.cell(category.description),
        rx.table.cell(category.date),
        rx.table.cell([category.subcategories]),
        rx.table.cell(
            rx.hstack(
                update_category_dialog(category),
                rx.button(
                    rx.icon("trash-2", size=22),
                    rx.text("Borrar", size="3"),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                    on_click=lambda: State.delete_category(getattr(category, "id")),
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )


def add_category_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar Categoria", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="album", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Agregar nueva categoría",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Completa el formulario con la información de la nueva categoría",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            label="Nombre",
                            placeholder="Nombre de Categoría",
                            type="text",
                            name="name",
                            icon="airplay",
                        ),
                        # Description
                        form_field(
                            label="Descripción", 
                            placeholder="Esta sección representa..",
                            type="text",
                            name="description",
                            icon="airplay",
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Categoria agregada"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_category_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def update_category_dialog(category):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Editar", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_category(category),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Editar categoría",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Edita la información de la categoría",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # Name
                        form_field(
                            label="Nombre",
                            placeholder="Nombre de Categoría",
                            type="text",
                            name="name",
                            icon="airplay",
                            default_value=category.name
                        ),
                        # Description
                        form_field(
                            label="Descripción", 
                            placeholder="Esta sección representa..",
                            type="text",
                            name="description",
                            icon="airplay",
                            default_value=category.description
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Modificar categoría"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.update_category_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            add_category_button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                ["name", "description", "date"],
                placeholder="Ordenar por Nombre",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Buscar aquí...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Nombre", "clipboard"),
                    _header_cell("Descripción", "clipboard-pen-line"),
                    _header_cell("Fecha", "calendar"),
                    _header_cell("Subcategorías", "ungroup"),
                    _header_cell("Acción", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.categories, show_category)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )