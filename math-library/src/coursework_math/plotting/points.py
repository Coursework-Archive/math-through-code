"""Plots and transformations based on discrete points."""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TypeAlias

import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np

from .axes import AXIS_COLOR, PRIMARY_LINE_COLOR
from .latex import label_latex

Point: TypeAlias = tuple[float, float]


def transform_points(
    points: Iterable[Point],
    *,
    x_mult: float = 1.0,
    x_negate: bool = False,
    y_mult: float = 1.0,
    y_negate: bool = False,
) -> list[Point]:
    """Apply horizontal and vertical scaling/reflection to points."""

    transformed: list[Point] = []
    for x_value, y_value in points:
        x_result = -x_value if x_negate else x_value
        y_result = -y_value if y_negate else y_value
        transformed.append((x_result * x_mult, y_result * y_mult))
    return transformed


def plot_data_points(
    x: Sequence[float],
    y: Sequence[float],
    *,
    connect: bool = True,
    marker: str = "o",
    title: str | None = None,
    xlabel: str = "x",
    ylabel: str = "y",
    show_grid: bool = True,
    tangent: bool = False,
    tangent_x0: float | None = None,
    tangent_y0: float | None = None,
    tangent_slope: float | None = None,
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Plot discrete data, optionally with a tangent-line illustration."""

    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    if not x:
        raise ValueError("x and y must not be empty")

    if tangent and None in (tangent_x0, tangent_y0, tangent_slope):
        raise ValueError(
            "tangent_x0, tangent_y0, and tangent_slope are required when tangent=True"
        )

    if ax is None:
        _, ax = plt.subplots()

    if connect:
        ax.plot(x, y, marker=marker, label="data")
    else:
        ax.scatter(x, y, marker=marker)

    if tangent:
        assert tangent_x0 is not None
        assert tangent_y0 is not None
        assert tangent_slope is not None
        tangent_x = [tangent_x0 - 1, tangent_x0 + 1]
        tangent_y = [
            tangent_y0 + tangent_slope * (value - tangent_x0)
            for value in tangent_x
        ]
        ax.plot(tangent_x, tangent_y, linestyle="--", linewidth=2, label="Tangent line")
        ax.scatter(tangent_x, tangent_y, s=70, zorder=5)
        for x_value, y_value in zip(tangent_x, tangent_y, strict=True):
            dx, dy = (8, -14) if x_value < tangent_x0 else (8, 8)
            ax.annotate(
                f"({x_value:.1f}, {y_value:.1f})",
                xy=(x_value, y_value),
                xytext=(dx, dy),
                textcoords="offset points",
                fontsize=9,
                ha="left",
                va="bottom" if dy > 0 else "top",
                zorder=6,
            )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    if show_grid:
        ax.grid(True)
    if show:
        plt.show()
    return ax


def plot_polyline(
    points: Iterable[Point],
    *,
    equation: str | None = None,
    marker: str = "o",
    color: str = PRIMARY_LINE_COLOR,
    latex_title: bool = True,
    display_latex: bool = False,
    latex_loc: str = "tl",
    latex_pad: float = 0.02,
    latex_fontsize: int = 13,
    xlim: tuple[float, float] | None = (-5, 5),
    ylim: tuple[float, float] | None = (-5, 5),
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Plot a connected set of points with an optional equation label."""

    point_list = list(points)
    if not point_list:
        raise ValueError("points must not be empty")

    x_values, y_values = zip(*point_list, strict=True)
    if ax is None:
        _, ax = plt.subplots(figsize=(6.5, 6.5))

    ax.axhline(0, color=AXIS_COLOR, linewidth=1.6, zorder=0)
    ax.axvline(0, color=AXIS_COLOR, linewidth=1.6, zorder=0)
    ax.plot(x_values, y_values, marker=marker, color=color, linewidth=2.2)
    ax.set_aspect("equal", adjustable="box")

    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    if equation:
        if display_latex:
            try:
                from IPython.display import Math, display
            except ImportError:  # pragma: no cover - environment dependent
                pass
            else:
                display(Math(equation))
        else:
            location_map = {
                "tl": (latex_pad, 1 - latex_pad, "left", "top"),
                "tr": (1 - latex_pad, 1 - latex_pad, "right", "top"),
                "bl": (latex_pad, latex_pad, "left", "bottom"),
                "br": (1 - latex_pad, latex_pad, "right", "bottom"),
            }
            if latex_loc not in location_map:
                raise ValueError("latex_loc must be one of: 'tl', 'tr', 'bl', 'br'")
            x_position, y_position, horizontal, vertical = location_map[latex_loc]
            label = rf"${label_latex(equation)}$" if latex_title else equation
            ax.text(
                x_position,
                y_position,
                label,
                transform=ax.transAxes,
                ha=horizontal,
                va=vertical,
                fontsize=latex_fontsize,
            )

    if xlim is not None and ylim is not None:
        ax.set_xticks(np.arange(xlim[0], xlim[1] + 0.5, 0.5), minor=True)
        ax.set_yticks(np.arange(ylim[0], ylim[1] + 0.5, 0.5), minor=True)
        ax.grid(True, which="minor", linestyle="--", linewidth=0.4, alpha=0.4)

    if show:
        plt.show()
    return ax
