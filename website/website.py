"""
This is the main module of the web app
"""

# 3pps
import reflex as rx

# define styles
style = {
    "font_family": "JetBrains Mono",
}
stylesheets = [
    "css/font.css",
]


app = rx.App(
    theme=rx.theme(appearance="dark", accent_color="violet"),
    style=style,  # type: ignore
    stylesheets=stylesheets,
)
