"""
This module contains the code to generate cards.
"""

# 3pps
import reflex as rx


def experience_card(
    title: str, company: str, logo_path: str, duration: str, description: rx.Component
) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.center(
                rx.image(src=logo_path, height="10em", justify_content="center"),  # Company logo
                width="100%",
            ),
            width="30%"
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(company, font_weight="bold", color="gray"),
            description,
            align="start",
        ),
        width="50%",
        spacing="9",
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
    )
