"""
This module contains the code for the publications.
"""

# 3pps
import reflex as rx

# Own modules
from website.components.menu import get_menu
from website.components.cards import publication_card


@rx.page(route="/publications", title="Oscar Llorente | Publications")  # type: ignore
def publications_page() -> rx.Component:
    """
    This function defines the publications page.

    Returns:
        Stack of elements for the page.
    """

    return rx.vstack(
        get_menu(),
        rx.vstack(
            rx.box(height="2em"),
            publication_card(
                "Methods and Apparatuses for using a Graph Neural Network to Determine"
                " Recommended Configurations for a Plurality of Nodes",
                [
                    "Oscar Llorente",
                    "Rana Fawzy",
                    "Victor Buenestado",
                    "Anderson Falci",
                    "Raul Martin Cuerdo",
                ],
                "Embodiments described herein relate to methods and apparatuses for"
                " using a Bayesian graph neural network, B-GNN, to determine"
                " recommended configurations for a plurality of nodes, wherein the"
                " B-GNN comprises the plurality of nodes and a plurality of edges, and"
                " wherein the B-GNN is trained to predict the one or more performance"
                " metrics associated with the plurality of nodes based on"
                " configurations applied to the plurality of nodes. A computer"
                " implemented method comprises performing an optimization process"
                " utilizing the B-GNN based on a process execution type to determine"
                " the recommended configurations for the plurality of nodes.",
                "/images/wipo_logo.png",
                "",
                "",
                "https://patentscope.wipo.int/search/en/detail.jsf?"
                "docId=WO2025090007&_cid=P20-MA6791-81263-18",
            ),
            publication_card(
                "Evaluating Neighbor Explainability for Graph Neural Networks",
                [
                    "Oscar Llorente",
                    "Rana Fawzy",
                    "Jared Keown",
                    "Michal Horemuz",
                    "Péter Vaderna",
                    "Sándor Laki",
                    "Roland Kotroczó",
                    "Rita Csoma",
                    "János Márk Szalai-Gindl",
                ],
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
                " to identify important neighbors when GNNs without self-loops are used"
                " (The code to replicate our findings will be available here:"
                " https://github.com/EricssonResearch/gnn-neighbors-xai).",
                "/images/springer_logo.png",
                "https://link.springer.com/chapter/10.1007/978-3-031-63787-2_20",
                "https://github.com/EricssonResearch/gnn-neighbors-xai",
            ),
            publication_card(
                "A matter of attitude: Focusing on positive and active gradients to"
                " boost saliency maps",
                ["Oscar Llorente", "Jaime Boal", "Eugenio F. Sánchez-Úbeda"],
                "Saliency maps have become one of the most widely used interpretability"
                " techniques for convolutional neural networks (CNN) due to their"
                " simplicity and the quality of the insights they provide. However,"
                " there are still some doubts about whether these insights are a"
                " trustworthy representation of what CNNs use to come up with their"
                " predictions. This paper explores how rescuing the sign of the"
                " gradients from the saliency map can lead to a deeper understanding of"
                " multi-class classification problems. Using both pretrained and"
                " trained from scratch CNNs we unveil that considering the sign and the"
                " effect not only of the correct class, but also the influence of the"
                " other classes, allows to better identify the pixels of the image that"
                " the network is really focusing on. Furthermore, how occluding or"
                " altering those pixels is expected to affect the outcome also becomes"
                " clearer.",
                "/images/arxiv_logo.png",
                "https://arxiv.org/abs/2309.12913",
                "https://github.com/osllogon/positive_active_saliency_maps",
            ),
            publication_card(
                "A Transformer approach for Electricity Price Forecasting",
                ["Oscar Llorente", "Jose Portela"],
                "This paper presents a novel approach to electricity price forecasting"
                " (EPF) using a pure Transformer model. As opposed to other"
                " alternatives, no other recurrent network is used in combination to"
                " the attention mechanism. Hence, showing that the attention layer is"
                " enough for capturing the temporal patterns. The paper also provides"
                " fair comparison of the models using the open-source EPF toolbox and"
                " provide the code to enhance reproducibility and transparency in EPF"
                " research. The results show that the Transformer model outperforms"
                " traditional methods, offering a promising solution for reliable and"
                " sustainable power system operation.",
                "/images/arxiv_logo.png",
                "https://arxiv.org/abs/2403.16108",
                "https://github.com/osllogon/epf-transformers",
            ),
            width="100%",
            spacing="0",
            align="center",
        ),
    )
