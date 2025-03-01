# 3pps
import reflex as rx


@rx.page(route="/publications")
def publications_page():
    return rx.text("Publications Page")
