# 3pps
import reflex as rx


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def get_menu() -> rx.Component:
    """
    This function returns the menu for the application.

    Returns:
        Menu component.
    """

    menu: rx.Component = rx.box(
        rx.hstack(
            navbar_icons_item("Home", "home", "/#"),
            navbar_icons_item("Experience", "book-open", "/experience"),
            navbar_icons_item("Publications", "flask-conical", "/publications"),
            navbar_icons_item("Talks", "mic-vocal", "/talks"),
            spacing="6",
            justify="center",
        ),
        align_items="center",
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )

    return menu
