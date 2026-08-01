"""Shared Matplotlib axis formatting."""

from __future__ import annotations

from collections.abc import Sequence

import matplotlib.axes
import numpy as np

PRIMARY_LINE_COLOR = "#7b6cff"
AXIS_COLOR = "#dddddd"
GRID_MAJOR_ALPHA = 0.6
GRID_MINOR_ALPHA = 0.4


def set_pi_ticks(
    ax: matplotlib.axes.Axes,
    ticks: Sequence[float] | None = None,
) -> None:
    """Label common x-axis locations as multiples of pi."""

    values = np.asarray(
        ticks if ticks is not None else [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
        dtype=float,
    )
    default_labels = {
        -np.pi: r"$-\pi$",
        -np.pi / 2: r"$-\frac{\pi}{2}$",
        0.0: r"$0$",
        np.pi / 2: r"$\frac{\pi}{2}$",
        np.pi: r"$\pi$",
    }
    labels = [default_labels.get(float(value), rf"${value / np.pi:g}\pi$") for value in values]
    ax.set_xticks(values)
    ax.set_xticklabels(labels)


def style_axes_origin_with_arrows(
    ax: matplotlib.axes.Axes,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    *,
    grid: bool = True,
) -> matplotlib.axes.Axes:
    """Move axes to the origin and draw arrowheads on positive directions."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if np.isclose(xlim[1] - xlim[0], 2 * np.pi, atol=1e-2):
        set_pi_ticks(ax)

    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    ax.spines["left"].set_linewidth(1.6)
    ax.spines["bottom"].set_linewidth(1.6)
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    ax.tick_params(axis="both", which="both", colors="black", labelsize=10)

    if grid:
        ax.grid(True, alpha=0.25, linewidth=1)

    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    ax.annotate(
        "",
        xy=(xlim[1], 0),
        xytext=(xlim[1] - 0.06 * x_range, 0),
        arrowprops={"arrowstyle": "->", "color": "black", "lw": 1.6},
        clip_on=False,
    )
    ax.annotate(
        "",
        xy=(0, ylim[1]),
        xytext=(0, ylim[1] - 0.06 * y_range),
        arrowprops={"arrowstyle": "->", "color": "black", "lw": 1.6},
        clip_on=False,
    )
    ax.text(xlim[1] - 0.08 * x_range, 0 + 0.04 * y_range, "x", color="black")
    ax.text(0 + 0.04 * x_range, ylim[1] - 0.10 * y_range, "y", color="black")
    return ax
