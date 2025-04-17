"""
This module contains the code to define buttons.
"""

# 3pps
import reflex as rx


def get_special_button(text: str, icon_name: str, url: str, color: str) -> rx.Component:
    """
    _summary_

    Returns:
        _description_
    """

    # Define button
    if url != "":
        button: rx.Component = rx.link(
            rx.button(
                rx.icon(icon_name),
                text,
                size="3",
                variant="surface",
                color_scheme=color,  # type: ignore
                cursor="pointer",
            ),
            href=url,
        )

    else:
        button = rx.button(
            rx.icon(icon_name),
            text,
            size="3",
            variant="surface",
            color_scheme=color,  # type: ignore
        )

    return button
