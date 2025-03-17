"""
This module contains the index page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import experience_card


@rx.page(route="/experience", title="Oscar Llorente | Home")
def experience_page() -> rx.Component:
    """
    This function defines the home page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.vstack(
            rx.box(height="2em"),
            experience_card(
                "Senior Data Scientist",
                "Ericsson, Jan 2024 - Present",
                "/images/logo.png",
                "Jan 2024 - Present",
                rx.vstack(
                    rx.text(
                        "Data Scientist at Ericsson Cognitive Network Solutions (JS6):"
                    ),
                    rx.list.unordered(  # type: ignore
                        rx.list.item(  # type: ignore
                            "Member of the Data Science Board, group of "
                            "experts who manage Machine Learning in the organization."
                        ),
                        rx.list.item(  # type: ignore
                            "Head of the Geometric Artificial Intelligence (GAI) Lab."
                        ),
                        rx.list.item(  # type: ignore
                            "Machine Learning Lead of the Uplink Optimizer 4G and 5G, "
                            "telecommunications network optimizer that improves the "
                            "uplink interference with Graph Neural Networks."
                        ),
                        list_style_type="circle",
                        style={  # type: ignore
                            "text_align": "justify",
                        },
                    ),
                ),
            ),
            experience_card(
                "Adjunct Professor",
                "Comillas Pontifical University (ICAI), Jan 2024 - Present",
                "/images/icai_logo.png",
                "Jan 2024 - Present",
                rx.vstack(
                    rx.text(
                        "Data Scientist at Ericsson Cognitive Network Solutions (JS6):"
                    ),
                    rx.list.unordered(  # type: ignore
                        rx.list.item(  # type: ignore
                            "Member of the Data Science Board, group of "
                            "experts who manage Machine Learning in the organization."
                        ),
                        rx.list.item(  # type: ignore
                            "Head of the Geometric Artificial Intelligence (GAI) Lab."
                        ),
                        rx.list.item(  # type: ignore
                            "Machine Learning Lead of the Uplink Optimizer 4G and 5G, "
                            "telecommunications network optimizer that improves the "
                            "uplink interference with Graph Neural Networks."
                        ),
                        list_style_type="circle",
                        style={  # type: ignore
                            "text_align": "justify",
                        },
                    ),
                ),
            ),
            experience_card(
                "Experienced Data Scientist",
                "Ericsson, Jun 2023 - Dec 2023",
                "/images/logo.png",
                "Jan 2024 - Present",
                rx.vstack(
                    rx.text(
                        "Data Scientist at Ericsson Cognitive Network Solutions (JS5):"
                    ),
                    rx.list.unordered(  # type: ignore
                        rx.list.item(  # type: ignore
                            "Machine Learning Lead of the Uplink Optimizer 4G and 5G, "
                            "telecommunications network optimizer that improves the "
                            "uplink interference with Graph Neural Networks."
                        ),
                        rx.list.item(  # type: ignore
                            "Creation of a internal library to handle datasets from S3 "
                            "bucket and AWS based in Boto3."
                        ),
                        list_style_type="circle",
                        style={  # type: ignore
                            "text_align": "justify",
                        },
                    ),
                ),
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
