"""
This module contains the education page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import education_card


@rx.page(route="/education", title="Oscar Llorente | Education")
def education_page() -> rx.Component:
    """
    This function defines the home page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.vstack(
            rx.box(height="2em"),
            education_card(
                "Doctor of Philosophy - PhD, Artificial Intelligence",
                "Comillas Pontifical University",
                "Jan 2024 - Present",
                "/images/icai_logo.png",
                "",
                [
                    "Thesis: Explainability in Graph Neural Networks",
                    "Collaboration: Ericsson Cognitive Labs",
                ],
            ),
            education_card(
                "Master of Science, Artificial Intelligence",
                "University of Carlos III of Madrid",
                "Sep 2022 - Sep 2024",
                "/images/carlos_logo.png",
                "",
                [
                    "Nova 111 Student List (best 111 students of Spain)",
                    "Thesis: Bayesian Graph Neural Networks: Confidence Intervals",
                    (
                        "Main courses: Deep Learning, Deep Learning II, "
                        "Natural Language Processing, AI for Medicine, AI for Finance"
                    ),
                    "GPA: 8.43/10",
                ],
            ),
            education_card(
                "Double Bachelor of Engineering - BE, Telecommunications "
                "Engineering & Business Analytics",
                "Comillas Pontifical University",
                "Sep 2017 - Jun 2022",
                "/images/icai_logo.png",
                "",
                [
                    (
                        "Telecommunications Engineering Thesis: Development of "
                        "visualization and interpretation tools for convolutional "
                        "neural networks"
                    ),
                    (
                        "Business Analytics: Electricity Price Forecasting with "
                        "Transformers"
                    ),
                    "EY Accésit for Business Analytics Thesis",
                    "GPA: 8.28/10",
                ],
            ),
            education_card(
                "Exchange Program, Computer Science",
                "University of Texas at Austin",
                "Sep 2020 - Jun 2021",
                "/images/texas_logo.png",
                "The main courses of the exchange are the following:",
                [
                    "Honor list in both semesters",
                    "Courses in Computer Science and Economics majors",
                    (
                        "Main courses: Deep Learning, Natural Language Processing, "
                        "Autonomous Driving, Algorithms and Complexity, "
                        "Ethical Hacking"
                    ),
                    "GPA: 3.82/4",
                ],
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
