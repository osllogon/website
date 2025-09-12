"""
This module contains the code to define buttons.
"""

# 3pps
import reflex as rx


def get_special_button(text: str, icon_name: str, url: str, color: str) -> rx.Component:
    """
    This functions gets special buttons.

    Returns:
        Component representing a button.
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


def get_talk_buttons(
    recording_url: str, source_url: str, slides_path: str, language: str
) -> list[rx.Component]:
    """
    This function gets the buttons for the talks page.

    Args:
        recording_url: Url of the recording.
        source_url: Source of the talk.
        slides_path: Path of the slides used in the talk.
        language: Language the talk was given.

    Returns:
        List of components.
    """

    # Init buttons list
    buttons: list[rx.Component] = []

    if recording_url != "":
        buttons.append(
            get_special_button(
                "Recording",
                "youtube",
                recording_url,
                "red",
            )
        )

    if source_url != "":
        buttons.append(
            get_special_button(
                "Source",
                "link",
                source_url,
                "amber",
            ),
        )

    if slides_path != "":
        buttons.append(
            get_special_button(
                "Slides",
                "presentation",
                slides_path,
                "indigo",
            ),
        )

    buttons.append(
        get_special_button(
            language,
            "languages",
            "",
            "jade",
        ),
    )

    return buttons


def get_course_buttons(url: str, path: str) -> list[rx.Component]:
    """
    This function computes the course buttons.

    Args:
        url: Url of the credential.
        path: Path of the credentials file.

    Returns:
        List of buttons.
    """

    # Define buttons
    buttons: list[rx.Component] = []

    if url != "":
        buttons.append(
            get_special_button(
                "URL",
                "link",
                url,
                "amber",
            ),
        )

    if path != "":
        buttons.append(
            get_special_button(
                "Path",
                "presentation",
                path,
                "indigo",
            ),
        )

    return buttons
