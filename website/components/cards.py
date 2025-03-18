"""
This module contains the code to generate cards.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.buttons import get_special_button


def experience_card(
    title: str,
    company: str,
    duration: str,
    logo_path: str,
    introduction: str,
    bullets: list[str],
) -> rx.Component:
    """
    This function creates a card for the experience section.
    
    Args:
        title: Title of the position.
        company: Company name.
        duration: String indicating the duration.
        logo_path: Path of the logo showed in the card.
        introduction: Introduction text for the description.
        bullets: List of bullet points for the description.

    Returns:
        Card for experience section.
    """

    return rx.hstack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width="25%",
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{company}, {duration}", font_weight="bold", color="gray"),
            get_description_experience(introduction, bullets),
            align="start",
            width="75%",
        ),
        width="50%",
        spacing="9",
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
        align_items="center",
    )


def publication_card(
    title: str,
    authors: list[str],
    abstract: str,
    paper_url: str,
    github_url: str,
    logo_path: str,
) -> rx.Component:
    """
    This function creates a card for the publications section.

    Args:
        title: Title of the publication.
        authors: List with the names of the authors.
        abstract: Text with the abstract of the publication.
        paper_url: Link to the publication.
        github_url: Link to the source code in GitHub.
        logo_path: Path of the logo to use in the card.

    Returns:
        Card for publications section.
    """
    
    return rx.hstack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width="25%",
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(
                f"{','.join(author for author in authors)}",
                font_weight="bold",
                color="gray",
            ),
            rx.scroll_area(
                rx.text(abstract, style={"text_align": "justify"}),  # type: ignore
                type="always",
                scrollbars="vertical",
                style={"height": 180},  # type: ignore
            ),
            rx.hstack(
                get_special_button(
                    "Manuscript",
                    "graduation-cap",
                    paper_url,
                    "amber",
                ),
                get_special_button(
                    "Source Code",
                    "github",
                    github_url,
                    "gray",
                ),
                margin_top="2%",
            ),
            align="start",
            width="75%",
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
    
    Args:
        introduction: Text as an introduction.
        bullets: List of texts to be showed as bullets points.

    Returns:
        Vertical stack with a brief description and a list of bullets
            to include.
    """

    return rx.vstack(
        rx.text(introduction),
        rx.list.unordered(  # type: ignore
            *[rx.list.item(bullet) for bullet in bullets],  # type: ignore
            list_style_type="circle",
            style={  # type: ignore
                "text_align": "justify",
            },
        ),
    )
