"""
This module contains the index page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu


@rx.page(route="/", title="Oscar Llorente | Home")
def index_page() -> rx.Component:
    return rx.box(
        get_menu(),
        rx.hstack(
            rx.flex(
                rx.image(
                    src="images/profile.jpeg",
                    alt="Profile",
                    border_radius="100%",
                    padding="6em",
                ),
            justify="end",
            width="50%"),
            rx.card(
                rx.vstack(
                    rx.heading("About me"),
                    rx.text(
                        "Hello there, first of all let's say it I define myself as a romantic of life. This means that I am excited about every aspect of life and try to bring that to each aspect of  I'm currently a Senior Data Scientist at Ericsson Cognitive Software Engineering. "
                        "Oscar is a Senior Data Scientist at Ericsson Cognitive Software Engineering. This department is , Head of the Geometric Artificial Intelligence (GAI) Lab. Currently, he is working on the optimization of cellular networks with Graph Neural Networks. Geometric Deep Learning and Explainability are his main research areas."
                    ),
                    rx.text("Now, talking about my work, currently I am a Senior Data Scientist at Ericsson. Specifically I work in a department called Cognitive Network Solutions that uses AI to diagnose the different problems of cellular networks and optimizes them. Since in Ericsson the term Data Scientist is a bit broad, let me explain what I do in day-to-day. "),
                    rx.text("Then, outside Ericsson I also work as an Adjunct Professor at the Comillas Pontifical University (ICAI), teaching a course on Deep Learning in Mathematical Engineering and Artificial Intelligence degree. I love teaching and, although my students will think for sure that I am too hard (maybe using other terms...), I view this as an opportunity to give back to the community, which is the duty I think we all have.")
                ),
                margin_top="3em",
                width="40%",
                justify="start"
            ),
            width="100%",
        ),
    )