"""
This module contains the code to generate cards.
"""

# 3pps
import reflex as rx


def experience_card(
    title: str, company: str, duration: str, logo_path: str, introduction: str, bullets: list[str]
) -> rx.Component:
    """
    This function creates a card for the experience section.

    Returns:
        Card for Experience section.
    """
    
    return rx.hstack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em"
                ),
            ),
            width="25%"
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{company}, {duration}", font_weight="bold", color="gray"),
            get_description_experience(introduction, bullets),
            align="start",
            width="75%"
        ),
        width="50%",
        spacing="9",
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
        align_items="center",
    )
    

def get_description_experience(introduction: str, bullets: list[str]) -> rx.Component:
    """
    This function defines a description to be included in an experience 
    card.

    Returns:
        Vertical stack with a brief description and a list of bullets 
            to include.
    """
    
    return rx.vstack(
        rx.text(introduction),
        rx.list.unordered(  # type: ignore
            *[rx.list.item(bullet) for bullet in bullets], # type: ignore
            list_style_type="circle",
            style={  # type: ignore
                "text_align": "justify",
            },
        ),
    )
