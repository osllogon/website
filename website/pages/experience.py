"""
This module contains the index page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import experience_card


@rx.page(route="/experience", title="Oscar Llorente | Experience")
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
                "Ericsson",
                "Jan 2024 - Present",
                "/images/ericsson_logo.png",
                "Data Scientist at Ericsson Cognitive Network Solutions (JS6):",
                [
                    (
                        "Member of the Data Science Board, group of experts who manage "
                        "Machine Learning in the organization."
                    ),
                    "Head of the Geometric Artificial Intelligence (GAI) Lab.",
                    (
                        "Machine Learning Lead of the Uplink Optimizer 4G and 5G, "
                        "telecommunications network optimizer that improves the "
                        "uplink interference with Graph Neural Networks."
                    ),
                ],
            ),
            experience_card(
                "Adjunct Professor",
                "Comillas Pontifical University (ICAI)",
                "Jan 2024 - Present",
                "/images/icai_logo.png",
                "Bachelor of Engineering, Mathematical Engineering & Artificial"
                " Intelligence (iMAT):",
                [
                    "Computer Vision II, Theory & Lab Professor (2024).",
                    "Deep Learning, Theory & Lab Professor (2024-2025).",
                    "Natural Language Processing (NLP), Lab Professor (2024).",
                ],
            ),
            experience_card(
                "Experienced Data Scientist",
                "Ericsson",
                "Jun 2023 - Dec 2023",
                "/images/ericsson_logo.png",
                "Data Scientist at Ericsson Cognitive Network Solutions (JS5):",
                [
                    (
                        "Machine Learning Lead of the Uplink Optimizer 4G and 5G, "
                        "telecommunications network optimizer that improves the uplink "
                        "interference with Graph Neural Networks."
                    ),
                ],
            ),
            experience_card(
                "Data Scientist",
                "Ericsson",
                "Jun 2022 - May 2023",
                "/images/ericsson_logo.png",
                "Data Scientist at Ericsson Cognitive Network Solutions (JS4):",
                [
                    (
                        "Data Scientist in Uplink Optimizer, telecommunications network"
                        " optimizer that improves the uplink interference with Graph"
                        " Neural Networks."
                    ),
                    "Expert Data Scientist in Graph Neural Networks.",
                ],
            ),
            experience_card(
                "Data Scientist Intern",
                "Ericsson",
                "Sep 2021 - May 2022",
                "/images/ericsson_logo.png",
                "Data Scientist Intern at Ericsson:",
                [
                    (
                        "Development and implementation of a NLP projects, document "
                        "similarity between internal inquiries to save time to other "
                        "departments"
                    ),
                    (
                        "Research project about detection of cybersecurity"
                        " vulnerabilities based on packages descriptions "
                    ),
                ],
            ),
            experience_card(
                "Software Engineer Intern",
                "Stemy Energy",
                "Sep 2020 - March 2021",
                "/images/stemy_logo.png",
                "Software Engineer Intern at Stemy Energy:",
                ["Backend and frontend development using Django framework."],
            ),
            experience_card(
                "Data Scientist Intern",
                "Management Solutions",
                "Jul 2020 - Aug 2020",
                "/images/management_solutions.svg",
                "Data Scientist Intern at Management Solutions:",
                ["development of an Auto Machine Learning tool."],
            ),
            experience_card(
                "Software Engineer Intern",
                "Telefonica",
                "Jan 2020 - Jun 2020",
                "/images/telefonica_logo.png",
                "Member of the Automation Lab. The mains tasks of the team were to "
                "analyze and develop automation tools for different departments inside "
                "Telefónica.",
                [],
            ),
            experience_card(
                "Software Engineer Intern",
                "Institute of Research in Technology (IIT)",
                "Jun 2019 - Dec 2019",
                "/images/icai_logo.png",
                "Intern for the development of an optimizer tool for filling containers"
                " and trucks.",
                [],
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
