# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu


@rx.page(route="/publications", title="Oscar Llorente | Home")
def publications_page() -> rx.Component:
    return rx.box(
        get_menu(),
    )
