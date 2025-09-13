"""
This module contains the education page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import certification_card


@rx.page(route="/certifications", title="Oscar Llorente | Certifications")
def certifications_page() -> rx.Component:
    """
    This function defines the courses page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.vstack(
            rx.box(height="2em"),
            certification_card(
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
            certification_card(
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
            certification_card(
                "Tensorflow Advanced Techniques Specialization",
                "DeepLearning.AI",
                "Jun 2025",
                "/images/deeplearning_logo.webp",
                "This Specialization is an advanced level in Tensorflow, exploring "
                "the different APIs and how to build more complicated models. It also "
                "has content about how to ship different models in production and "
                "research topics as explainability.",
                "https://www.coursera.org/account/accomplishments/specialization/"
                "CCAC7XEJLW96?utm_source=link&utm_medium=certificate&utm_content="
                "cert_image&utm_campaign=sharing_cta&utm_product=s12n",
                "",
            ),
            certification_card(
                "Backend Experienced",
                "Ericsson",
                "Jan 2025",
                "/images/ericsson_logo.png",
                "This certification is the medium-level recognition level in Backend"
                " inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/92c029bd-fd5e-45f0-85b7-3e5ab9526d7b/"
                "public_url",
                "",
            ),
            certification_card(
                "Global Tech Talent",
                "Ericsson",
                "Jun 2024",
                "/images/ericsson_logo.png",
                "This course is to prepare future technical talent inside Ericsson. "
                "It is one of the most important courses for technical leadership "
                "inside the company.",
                "https://www.credly.com/badges/b9e83fa3-e216-482c-b398-77eaa8ad61af/"
                "public_url",
                "",
            ),
            certification_card(
                "Cloud Security Experienced",
                "Ericsson",
                "Aug 2023",
                "/images/ericsson_logo.png",
                "This certification is the medium-level recognition level in Cloud"
                " Security inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/e1088ccd-6ed7-4697-b43c-3871c2b453f4/"
                "public_url",
                "",
            ),
            certification_card(
                "Cloud Native Experienced",
                "Ericsson",
                "May 2023",
                "/images/ericsson_logo.png",
                "This certification is the medium-level recognition level in Cloud"
                " Native inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/be8ca76b-201b-4759-8c78-7dea05c0be17/"
                "public_url",
                "",
            ),
            certification_card(
                "Tensorflow Developer Specialization",
                "DeepLearning.AI",
                "Apr 2023",
                "/images/deeplearning_logo.webp",
                "This Specialization prepares for a basic knowledge in Tensorflow, "
                "introducing the different APIs and basic use cases that can be "
                "developed with it.",
                "https://www.coursera.org/account/accomplishments/specialization/"
                "certificate/N3BKPS4YVUQX",
                "",
            ),
            certification_card(
                "Backend Fundamental",
                "Ericsson",
                "Feb 2023",
                "/images/ericsson_logo.png",
                "This certification is the fundamental-level recognition level in "
                "Backend inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/f8738b19-ee22-47cb-ab2b-eaf669d09161/"
                "public_url",
                "",
            ),
            certification_card(
                "SW R&D 5G Fundamental",
                "Ericsson",
                "Feb 2023",
                "/images/ericsson_logo.png",
                "This certification is the fundamental-level recognition level in "
                "Radio inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/daf099fd-d4e8-43ce-ba08-1ebaf1b0da12/"
                "public_url",
                "",
            ),
            certification_card(
                "Cloud Fundamental",
                "Ericsson",
                "Nov 2022",
                "/images/ericsson_logo.png",
                "This certification is the fundamental-level recognition level in "
                "Cloud inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/4917f45b-a856-47bd-a643-b2fc294a3025/"
                "public_url",
                "",
            ),
            certification_card(
                "Machine Learning Experienced",
                "Ericsson",
                "Nov 2022",
                "/images/ericsson_logo.png",
                "This certification is the medium-level recognition level in Machine"
                " Learning inside Ericsson Business Cloud & Software Services (BCSS).",
                "https://www.credly.com/badges/04cba84b-3346-486e-b495-"
                "3883f56f156c/public_url",
                "",
            ),
            certification_card(
                "Machine Learning Specialization",
                "Stanford University",
                "Nov 2022",
                "/images/stanford_logo.png",
                "This Specialization is about an introductory level for Machine "
                "Learning. In this course they teach the classical ML algorithms, and "
                "how to use them in real use cases.",
                "https://www.coursera.org/account/accomplishments/specialization/"
                "8AR55FQV8R9H?utm_source=link&utm_medium=certificate&utm_content="
                "cert_image&utm_campaign=sharing_cta&utm_product=s12n",
                "",
            ),
            certification_card(
                "Machine Learning Fundamental",
                "Ericsson",
                "Nov 2022",
                "/images/ericsson_logo.png",
                "This certification is the fundamental-level recognition level in "
                "Machine Learning inside Ericsson Business Cloud & Software Services "
                "(BCSS).",
                "https://www.credly.com/badges/89bc9394-3685-4bec-9e27-b2eaad24bd00",
                "",
            ),
            certification_card(
                "Deep Learning Specialization",
                "DeepLearning.AI",
                "Mar 2021",
                "/images/deeplearning_logo.webp",
                "This Specialization gives you an introducotry level in Deep "
                "Learning, studying the foundations behind the different techniques "
                "you may use in real use cases. ",
                "https://www.coursera.org/account/accomplishments/specialization/"
                "ALXBVJ33EFWQ",
                "",
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
