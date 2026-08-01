"""Reusable utilities for mathematics coursework."""

from .images import load_image, show_image
from .plotting import (
    display_equation,
    display_latex,
    epsilon_delta_plot,
    equation_latex,
    label_latex,
    plot_data_points,
    plot_equation,
    plot_piecewise,
    plot_polyline,
    set_pi_ticks,
    style_axes_origin_with_arrows,
    transform_points,
)

__version__ = "0.1.0"

__all__ = [
    "display_equation",
    "display_latex",
    "epsilon_delta_plot",
    "equation_latex",
    "label_latex",
    "load_image",
    "plot_data_points",
    "plot_equation",
    "plot_piecewise",
    "plot_polyline",
    "set_pi_ticks",
    "show_image",
    "style_axes_origin_with_arrows",
    "transform_points",
]
