"""
This module contains the reflex configuration.
"""

# 3pps
import reflex as rx

# Define configuration
config = rx.Config(
    app_name="website",
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)
