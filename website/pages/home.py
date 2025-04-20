"""
This module contains the index page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.buttons import get_special_button


@rx.page(route="/", title="Oscar Llorente | Home")
def home_page() -> rx.Component:
    """
    This function defines the home page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.hstack(
            rx.vstack(
                rx.flex(
                    rx.image(
                        src="images/profile.jpeg",
                        alt="Profile",
                        border_radius="100%",
                        padding="6em",
                    ),
                    justify="center",
                    align="center",
                    width="100%",
                ),
                rx.hstack(
                    get_special_button(
                        "Linkedin",
                        "linkedin",
                        "https://www.linkedin.com/in/osllogon",
                        "blue",
                    ),
                    get_special_button(
                        "GitHub", "github", "https://github.com/osllogon", "gray"
                    ),
                    get_special_button(
                        "Scholar",
                        "graduation-cap",
                        "https://scholar.google.es/citations?user=AL2xF9AAAAAJ&hl=en",
                        "amber",
                    ),
                    get_special_button(
                        "Gmail",
                        "mail",
                        "mailto:oscar.llorente.gonzalez@ericsson.com",
                        "red",
                    ),
                    get_special_button(
                        "Outlook",
                        "mail",
                        "mailto:oscar.llorente.gonzalez@ericsson.com",
                        "indigo",
                    ),
                    get_special_button("CV", "sticky-note", "files/CV.pdf", "green"),
                    justify="center",
                    align="center",
                    width="100%",
                ),
                width="50%",
            ),
            rx.card(
                rx.vstack(
                    rx.heading("About me"),
                    rx.text(
                        "Hello there, and I am just a curious person who wants to"
                        " contribute with something meaningful."
                    ),
                    rx.text(
                        "Now, about my work, currently I am a Senior Data Scientist at"
                        " Ericsson. Specifically, I work in a department called"
                        " Cognitive Network Solutions that uses AI to diagnose"
                        " the different problems of cellular networks and optimizes"
                        " them. Since in Ericsson the term Data Scientist is a bit"
                        " broad, let me explain what I do in my day-to-day. I think in"
                        " fact this would be closer to what a Research Scientist does,"
                        " since my work is focused in creating prototypes using"
                        " technologies as Graph Neural Networks, Deep Learning"
                        " Explainability or Bayesian Neural Networks. Specifically, I"
                        " am one of the Machine Learning leads of the organization,"
                        " driving the research part of several teams. And, finally, one"
                        " of the parts that I am most proud of: I am one of the"
                        " founders of Ericsson Cognitive Labs, our open-source"
                        " initiative to release part of our research open-source. There"
                        " I am the Head of the Geometric Artificial Intelligence (GAI)"
                        " Lab, which is specially focused in Graph Neural Networks."
                    ),
                    rx.text(
                        "Then, outside Ericsson I also work as an Adjunct Professor at"
                        " the Comillas Pontifical University (ICAI), teaching a course"
                        " on Deep Learning in Mathematical Engineering and Artificial"
                        " Intelligence degree. I love teaching and, although my"
                        " students will think for sure that I am too hard (maybe they"
                        " use other terms to explain it...), I view this as an"
                        " opportunity to give back to the community, which is the duty"
                        " I think we all have."
                    ),
                ),
                size="5",
                margin_top="3em",
                width="40%",
                justify="start",
                style={  # type: ignore
                    "text_align": "justify",
                },
            ),
            width="100%",
        ),
    )
