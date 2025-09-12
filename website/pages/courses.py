"""
This module contains the education page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import course_card


@rx.page(route="/courses", title="Oscar Llorente | Courses")
def courses_page() -> rx.Component:
    """
    This function defines the courses page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.button(
            "Download",
            on_click=rx.download(url="/images/ericsson_logo.png"),
        ),
        rx.vstack(
            rx.box(height="2em"),
            course_card(
                "Machine Learning Advanced",
                "Ericsson",
                "Jul 2025",
                "/images/ericsson_logo.png",
                "This certification is the highest-level recognition level in Machine"
                " Learning inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/04cba84b-3346-486e-b495-"
                "3883f56f156c/public_url",
                "",
            ),
            course_card(
                "Leaders Core Curriculum",
                "Ericsson",
                "Jun 2025",
                "/images/ericsson_logo.png",
                "This program covers the skills and capabilities required in the role"
                " of a line leader, project manager, or technical expert, leading,"
                " engaging, and developing participants in formal or project teams.",
                "",
                "/files/leaders_core_curriculum.jpeg",
            ),
            course_card(
                "Machine Learning Experienced",
                "Ericsson",
                "Jul 2025",
                "/images/ericsson_logo.png",
                "This certification is the medium-level recognition level in Machine"
                " Learning inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/04cba84b-3346-486e-b495-"
                "3883f56f156c/public_url",
                "",
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
