"""
This module contains the code to generate cards.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.buttons import (
    get_special_button,
    get_talk_buttons,
    get_course_buttons,
)


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

    return rx.stack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width=rx.breakpoints(initial="75%", xs="75%", sm="75%", md="25%", lg="25%"),
            padding=rx.breakpoints(initial="5%", xs="5%", sm="5%", md="0%", lg="0%"),
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{company}, {duration}", font_weight="bold", color="gray"),
            get_description_experience(introduction, bullets),
            align="start",
            width="75%",
        ),
        direction=rx.breakpoints(
            initial="column", xs="column", sm="column", md="row", lg="row"
        ),
        width=rx.breakpoints(initial="90%", xs="90%", sm="90%", md="50%", lg="50%"),
        spacing=rx.breakpoints(initial="3", xs="3", sm="3", md="9", lg="9"),
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
        align_items="center",
    )


def education_card(
    title: str,
    university: str,
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

    return rx.stack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width=rx.breakpoints(initial="75%", xs="75%", sm="75%", md="25%", lg="25%"),
            padding=rx.breakpoints(initial="5%", xs="5%", sm="5%", md="0%", lg="0%"),
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{university}, {duration}", font_weight="bold", color="gray"),
            get_description_experience(introduction, bullets),
            align="start",
            width="75%",
        ),
        direction=rx.breakpoints(
            initial="column", xs="column", sm="column", md="row", lg="row"
        ),
        width=rx.breakpoints(initial="90%", xs="90%", sm="90%", md="50%", lg="50%"),
        spacing=rx.breakpoints(initial="3", xs="3", sm="3", md="9", lg="9"),
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

    return rx.stack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width=rx.breakpoints(initial="75%", xs="75%", sm="75%", md="25%", lg="25%"),
            padding=rx.breakpoints(initial="5%", xs="5%", sm="5%", md="0%", lg="0%"),
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
                style=rx.breakpoints(
                    initial={"height": 270},
                    xs={"height": 270},
                    sm={"height": 270},
                    md={"height": 180},
                    lg={"height": 180},
                ),  # type: ignore
            ),
            rx.stack(
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
                width="100%",
                direction=rx.breakpoints(
                    initial="column", xs="column", sm="column", md="row", lg="row"
                ),
                align_items=rx.breakpoints(
                    initial="center", xs="center", sm="center", md="start", lg="start"
                ),
            ),
            align="start",
            width="75%",
        ),
        direction=rx.breakpoints(
            initial="column", xs="column", sm="column", md="row", lg="row"
        ),
        width=rx.breakpoints(initial="90%", xs="90%", sm="90%", md="50%", lg="50%"),
        spacing=rx.breakpoints(initial="3", xs="3", sm="3", md="9", lg="9"),
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
        align_items="center",
    )


def talk_card(
    title: str,
    organizer: str,
    date: str,
    logo_path: str,
    abstract: str,
    recording_url: str,
    source_url: str,
    slides_path: str,
    language: str,
) -> rx.Component:
    """
    This function creates a card for the talks section.

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

    return rx.stack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width=rx.breakpoints(initial="75%", xs="75%", sm="75%", md="25%", lg="25%"),
            padding=rx.breakpoints(initial="5%", xs="5%", sm="5%", md="0%", lg="0%"),
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{organizer}, {date}", font_weight="bold", color="gray"),
            rx.scroll_area(
                rx.text(abstract, style={"text_align": "justify"}),  # type: ignore
                type="always",
                scrollbars="vertical",
                style=rx.breakpoints(
                    initial={"height": 270},
                    xs={"height": 270},
                    sm={"height": 270},
                    md={"height": 180},
                    lg={"height": 180},
                ),
            ),
            rx.stack(
                *get_talk_buttons(recording_url, source_url, slides_path, language),
                margin_top="2%",
                width="100%",
                direction=rx.breakpoints(
                    initial="column", xs="column", sm="column", md="row", lg="row"
                ),
                align_items=rx.breakpoints(
                    initial="center", xs="center", sm="center", md="start", lg="start"
                ),
            ),
            align="start",
            width="75%",
        ),
        direction=rx.breakpoints(
            initial="column", xs="column", sm="column", md="row", lg="row"
        ),
        width=rx.breakpoints(initial="90%", xs="90%", sm="90%", md="50%", lg="50%"),
        spacing=rx.breakpoints(initial="3", xs="3", sm="3", md="9", lg="9"),
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


def certification_card(
    title: str,
    company: str,
    date: str,
    logo_path: str,
    abstract: str,
    url: str,
    file_path: str,
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

    return rx.stack(
        rx.box(
            rx.center(
                rx.image(
                    src=logo_path,
                    justify_content="center",
                    aspect_ratio="initial",
                    max_height="10em",
                ),
            ),
            width=rx.breakpoints(initial="75%", xs="75%", sm="75%", md="25%", lg="25%"),
            padding=rx.breakpoints(initial="5%", xs="5%", sm="5%", md="0%", lg="0%"),
        ),
        rx.vstack(
            rx.heading(title, size="4"),
            rx.text(f"{company}, {date}", font_weight="bold", color="gray"),
            rx.scroll_area(
                rx.text(abstract, style={"text_align": "justify"}),  # type: ignore
                type="always",
                scrollbars="vertical",
                style={"height": 75},  # type: ignore
            ),
            rx.hstack(
                *get_course_buttons(url, file_path),
                margin_top="2%",
            ),
            align="start",
            width="75%",
        ),
        direction=rx.breakpoints(
            initial="column", xs="column", sm="column", md="row", lg="row"
        ),
        width=rx.breakpoints(initial="90%", xs="90%", sm="90%", md="50%", lg="50%"),
        spacing=rx.breakpoints(initial="3", xs="3", sm="3", md="9", lg="9"),
        border_top=f"1.5px solid {rx.color('violet', 6)}",
        padding="2%",
        align_items="center",
    )
