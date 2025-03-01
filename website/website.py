"""
This is the main module of the web app
"""

# 3pps
import reflex as rx

# Own libraries
from rxconfig import config
from website.publications import publications_page


def navbar_icons_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )


def navbar_icons_menu_item(text: str, icon: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16),
            rx.text(text, size="3", weight="medium"),
        ),
        href=url,
    )


def index() -> rx.Component:
    return rx.box(
        rx.hstack(
            navbar_icons_item("Home", "home", "/#"),
            navbar_icons_item("Experience", "book-open", "/#"),
            navbar_icons_item("Publications", "flask-conical", "/publications"),
            navbar_icons_item("Talks", "mic-vocal", "/#"),
            spacing="6",
            justify="center",
        ),
        align_items="center",
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        font_family="JetBrains Mono",
        stylesheets=[
            "css/font.css",
        ],
    )


app = rx.App(theme=rx.theme(appearance="dark", accent_color="violet"))
app.add_page(index)
