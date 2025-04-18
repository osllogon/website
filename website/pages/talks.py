"""
This module contains the index page.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import talk_card


@rx.page(route="/talks", title="Oscar Llorente | Talks")
def talks_page() -> rx.Component:
    """
    This function defines the home page of the website.

    Returns:
        Vertical stack of the components of the page.
    """

    return rx.vstack(
        get_menu(),
        rx.vstack(
            rx.box(height="2em"),
            talk_card(
                "How to use Graph Neural Networks to optimize telecommunications"
                " networks",
                "PyData Madrid",
                "Feb 2025",
                "/images/pydata_logo.png",
                "Graph Neural Networks are a recent branch of deep learning, used to model complex data structures that can be interpreted as graphs. In this talk we introduce the concept, explaining how to build these type of models and evaluating the available frameworks. Moreover, we explain a real use case, how we can use these models to optimize the cellular networks.",
                "https://www.youtube.com/live/JE1W22_XdEc?si=V2_i58-xFy8ymvKO&t=3385",
                "https://guild.host/events/embeddings-para-contratacin-306046050",
                "files/pydata_feb_2025.pptx",
                "Spanish",
            ),
            talk_card(
                "Evaluating Neighbor Explainability for Graph Neural Networks",
                "XAI Global Conference",
                "July 2024",
                "/images/xai_conference_logo.png",
                "Graph Neural Networks (GNNs) have rapidly emerged as powerful tools"
                " for modeling complex data structures, particularly in the context of"
                " telecommunications, chemistry and social networking. Explainability"
                " in GNNs holds essential significance as it empowers stakeholders to"
                " gain insights into the inner workings of these complex models,"
                " fostering trust and transparency in decision-making processes. In"
                " this publication, we address the problem of determining how important"
                " is each neighbor for the GNN when classifying a node and how to"
                " measure the performance for this specific task. To do this, various"
                " known explainability methods are reformulated to calculate the"
                " neighbor importance and four new metrics, that aid in determining an"
                " explainability method’s reliability, are presented. Our results show"
                " that there is almost no difference between the explanations provided"
                " by gradient-based techniques in the GNN domain, in contrast to other"
                " areas of deep learning where this is an active area of research. This"
                " means that efforts in this direction may not produce such promising"
                " results for GNNs. In addition, many explainability techniques failed"
                " to identify important neighbors when GNNs without self-loops are"
                " used.",
                "",
                "https://xaiworldconference.com/2024/timetable/event/s-17-a-1-2-2-2-3/",
                "files/xai_conference.pdf",
                "English",
            ),
            talk_card(
                "Bayesian Graph Neural Networks, how to optimize a cellular network and"
                " provide confidence to our customers",
                "Learning on Graphs Conference (LoG) Madrid",
                "Nov 2023",
                "/images/log_logo.png",
                "Cellular networks are a certain type of telecommunications networks"
                " that can be easily modelled as a graph, which bring us the"
                " possibility of using a GNN to optimize it. First, we can construct a"
                " model to predict a performance indicator correlated with the problem"
                " we are trying to solve, using as inputs fixed variables and the"
                " configuration parameters we can change to improve the network, being"
                " able to model the relation between neighbor cells thanks to the"
                " structure of the GNN. Then, we can use any type of algorithm to"
                " optimize the parameters of each cell to improve the performance"
                " indicator of the model, also optimizing the real network if the model"
                " is accurate enough. Moreover, by redefining the model as a Bayesian"
                " Neural Network we can combine the accurate prediction of GNNs with"
                " the possibilities that probabilistic models bring to us. As an"
                " example, by defining the weights of the GNN as gaussian"
                " distributions, we can build a probabilistic model to construct"
                " confidence intervals of the expected gain that the optimization will"
                " bring, rather than a single prediction.",
                "https://tv.urjc.es/video/656875f1f8ceb7494b770b62",
                "https://logmeetupmadrid.github.io/",
                "files/log.pptx",
                "English",
            ),
            talk_card(
                "Solutions and challenges to optimize a cellular network with Graph"
                " Neural Networks",
                "Stanford Graph Learning Workshop (Poster)",
                "Oct 2023",
                "/images/stanford_logo.png",
                "Optimizing cellular networks has been a very difficult task for a long"
                " time. In these networks multiple problematic issues appear and the"
                " high number of parameters and variables to optimize makes it a"
                " difficult problem even for radio experts. Here an optimizer for a"
                " cellular network is presented, the Uplink Interference Optimizer."
                " Specifically, the uplink interference problem (degradation of the"
                " signal transmitted from a user terminal to a base station) will be"
                " solved by constructing a model that predicts a variable that reflects"
                " the interference level (SINR) and then optimizing the parameters of"
                " the cellular network, based on the model that has been built, to"
                " reduce it. That way, we achieve the optimization in a single step,"
                " improving previous solutions based on RL that must iterate over the"
                " real cellular network for several weeks. The simulator model will be"
                " based on Graph Neural Networks (constructed with PyTorch and PyTorch"
                " Geometric), allowing us to consider the neighborhood of a cell to"
                " make a prediction, which enhances the prediction accuracy over all"
                " older models. Then, any algorithm could be run to improve the"
                " parameters based on the simulator model we have constructed.",
                "https://www.youtube.com/clip/Ugkxdv8jC2XfIEm-a5R0OP__3gTySzzbeq-D",
                "https://snap.stanford.edu/graphlearning-workshop-2023/",
                "files/stanford.pptx",
                "English",
            ),
            talk_card(
                "Uplink Interference Optimizer, How to Optimize a Cellular Network in a"
                " Single Shot with GNNs",
                "PyTorch Conference",
                "Oct 2023",
                "/images/pytorch_logo.png",
                "Optimizing cellular networks has been a very difficult task for a long"
                " time. In these networks multiple problematic issues appear and the"
                " high number of parameters and variables to optimize makes it a"
                " difficult problem even for radio experts. Here an optimizer for a"
                " cellular network is presented, the Uplink Interference Optimizer."
                " Specifically, the uplink interference problem (degradation of the"
                " signal transmitted from a user terminal to a base station) will be"
                " solved by constructing a model that predicts a variable that reflects"
                " the interference level (SINR) and then optimizing the parameters of"
                " the cellular network, based on the model that has been built, to"
                " reduce it. That way, we achieve the optimization in a single step,"
                " improving previous solutions based on RL that must iterate over the"
                " real cellular network for several weeks. The simulator model will be"
                " based on Graph Neural Networks (constructed with PyTorch and PyTorch"
                " Geometric), allowing us to consider the neighborhood of a cell to"
                " make a prediction, which enhances the prediction accuracy over all"
                " older models. Then, any algorithm could be run to improve the"
                " parameters based on the simulator model we have constructed.",
                "https://www.youtube.com/watch?v=c96UxNyHuRo",
                "",
                "files/pytorch_conf.pptx",
                "English",
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
