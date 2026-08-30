"""Triangle plotting helpers for trigonometry coursework."""

from __future__ import annotations

from math import atan2, cos, degrees, radians, sin

import matplotlib.axes
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle

from .latex import label_latex


def plot_right_triangle(
    *,
    adjacent_label: str,
    opposite_label: str,
    hypotenuse_label: str,
    angle_label: str = r"\theta",
    title: str | None = None,
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Plot and label a right triangle for trig-substitution work.

    The diagram is symbolic rather than numerically scaled. The supplied
    strings describe the three sides relative to the angle at the
    lower-left corner.

    Parameters
    ----------
    adjacent_label:
        Label for the side adjacent to the angle.
    opposite_label:
        Label for the side opposite the angle.
    hypotenuse_label:
        Label for the hypotenuse.
    angle_label:
        Label for the reference angle.
    title:
        Optional title shown above the diagram.
    ax:
        Existing Matplotlib axes. A new figure is created when omitted.
    show:
        Whether to immediately display the figure.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the triangle.
    """

    if ax is None:
        _, ax = plt.subplots(figsize=(4, 3))

    # Fixed coordinates keep the symbolic triangle easy to read.
    left = (0.0, 0.0)
    right = (4.0, 0.0)
    top = (4.0, 3.0)

    # Draw all three sides as one connected line.
    ax.plot(
        [left[0], right[0], top[0], left[0]],
        [left[1], right[1], top[1], left[1]],
        linewidth=2,
    )

    # Mark the right angle.
    marker_size = 0.35
    right_angle = Rectangle(
        (right[0] - marker_size, right[1]),
        marker_size,
        marker_size,
        fill=False,
        linewidth=1.5,
    )
    ax.add_patch(right_angle)

    # Mark theta at the lower-left vertex.
    triangle_angle = degrees(
        atan2(top[1] - left[1], top[0] - left[0])
    )

    angle_arc = Arc(
        left,
        width=1.2,
        height=1.2,
        theta1=0,
        theta2=triangle_angle,
        linewidth=1.5,
    )
    ax.add_patch(angle_arc)

    angle_midpoint = radians(triangle_angle / 2)
    ax.text(
        0.85 * cos(angle_midpoint),
        0.85 * sin(angle_midpoint),
        rf"${label_latex(angle_label)}$",
        fontsize=14,
        ha="center",
        va="center",
    )

    # Side labels.
    ax.text(
        2.0,
        -0.25,
        rf"${label_latex(adjacent_label)}$",
        fontsize=14,
        ha="center",
        va="top",
    )

    ax.text(
        4.2,
        1.5,
        rf"${label_latex(opposite_label)}$",
        fontsize=14,
        ha="left",
        va="center",
    )

    ax.text(
        1.8,
        1.7,
        rf"${label_latex(hypotenuse_label)}$",
        fontsize=14,
        ha="center",
        va="bottom",
        rotation=triangle_angle,
    )

    if title:
        ax.set_title(title)

    ax.set_xlim(-0.5, 5.2)
    ax.set_ylim(-0.6, 3.8)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    if show:
        plt.show()

    return ax