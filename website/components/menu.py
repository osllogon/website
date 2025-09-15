"""
This module defines the menu.
"""

# 3pps
import reflex as rx


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    """
    This function created the icons to be used in the menu.

    Args:
        text: Text of the item.
        icon: Icon to use.
        url: Url of the page.

    Returns:
        Link element to be used in the menu.
    """

    return rx.link(
        rx.stack(
            rx.mobile_and_tablet(rx.icon(icon, size=32)),
            rx.desktop_only(rx.icon(icon)),
            rx.desktop_only(rx.text(text, size="4", weight="medium")),
            direction=rx.breakpoints(
                initial="column", xs="column", sm="column", md="row", lg="row"
            ),
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
            navbar_icons_item("Experience", "cog", "/experience"),
            navbar_icons_item("Education", "university", "/education"),
            navbar_icons_item("Publications", "flask-conical", "/publications"),
            navbar_icons_item("Talks", "mic-vocal", "/talks"),
            navbar_icons_item("Certifications", "monitor-cog", "/certifications"),
            spacing="6",
            justify="center",
        ),
        align_items="center",
        bg=rx.color("accent", 3),
        padding="1em",
        width="100%",
    )

    return menu
