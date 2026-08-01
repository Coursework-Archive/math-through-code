"""Public plotting API for coursework notebooks."""

from .axes import set_pi_ticks, style_axes_origin_with_arrows
from .equations import plot_equation
from .latex import display_equation, display_latex, equation_latex, label_latex
from .limits import epsilon_delta_plot
from .piecewise import Interval, Piece, plot_piecewise
from .points import Point, plot_data_points, plot_polyline, transform_points

__all__ = [
    "Interval",
    "Piece",
    "Point",
    "display_equation",
    "display_latex",
    "epsilon_delta_plot",
    "equation_latex",
    "label_latex",
    "plot_data_points",
    "plot_equation",
    "plot_piecewise",
    "plot_polyline",
    "set_pi_ticks",
    "style_axes_origin_with_arrows",
    "transform_points",
]
