"""Limit and epsilon-delta visualizations."""

from __future__ import annotations

from collections.abc import Callable

import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np

from .axes import style_axes_origin_with_arrows


def epsilon_delta_plot(
    function: Callable[[np.ndarray | float], np.ndarray | float],
    a: float,
    limit: float,
    eps: float = 0.5,
    delta: float = 0.5,
    xlim: tuple[float, float] = (-5, 5),
    ylim: tuple[float, float] = (-10, 10),
    title: str = "",
    *,
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Visualize an epsilon band and a corresponding delta neighborhood."""

    if eps <= 0 or delta <= 0:
        raise ValueError("eps and delta must be positive")
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))

    x_values = np.linspace(*xlim, 1200)
    y_values = np.asarray(function(x_values), dtype=float)
    if y_values.shape == ():
        y_values = np.full_like(x_values, y_values, dtype=float)

    ax.plot(x_values, y_values, linewidth=2)
    style_axes_origin_with_arrows(ax, xlim, ylim, grid=True)

    for y_target in (limit + eps, limit - eps):
        finite = np.isfinite(y_values)
        if not finite.any():
            continue
        finite_x = x_values[finite]
        finite_y = y_values[finite]
        x_hit = finite_x[np.argmin(np.abs(finite_y - y_target))]
        ax.plot([0, x_hit], [y_target, y_target], linestyle="--", linewidth=1.6)

    for x_delta in (a - delta, a + delta):
        y_hit = float(function(x_delta))
        ax.plot([x_delta, x_delta], [0, y_hit], linestyle="--", linewidth=1.6)

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(False)

    current_ticks = list(ax.get_xticks())
    ax.set_xticks(sorted({*current_ticks, a - delta, a, a + delta}))

    y_range = ylim[1] - ylim[0]
    x_range = xlim[1] - xlim[0]
    y_text = 0.03 * y_range
    x_stagger = 0.03 * x_range
    ax.text(a - delta - x_stagger, y_text, "a − δ", ha="center", va="bottom")
    ax.text(a, y_text, "a", ha="center", va="bottom")
    ax.text(a + delta + x_stagger, y_text, "a + δ", ha="center", va="bottom")
    ax.text(xlim[0] + 0.02 * x_range, limit + eps, "L + ε", va="bottom")
    ax.text(xlim[0] + 0.02 * x_range, limit - eps, "L − ε", va="top")

    if title:
        ax.set_title(title)
    if show:
        plt.show()
    return ax
