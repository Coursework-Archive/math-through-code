"""Piecewise function plotting."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypeAlias

import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from .axes import style_axes_origin_with_arrows

Interval: TypeAlias = tuple[float, float, bool, bool]
Piece: TypeAlias = tuple[sp.Expr, Interval]


def _major_spacing(span: float) -> float:
    if span > 100:
        return 20
    if span > 50:
        return 10
    if span > 20:
        return 5
    if span > 8:
        return 1
    return max(span / 6, 0.25)


def plot_piecewise(
    pieces: Iterable[Piece],
    *,
    var: sp.Symbol | None = None,
    num: int = 400,
    xlim: tuple[float, float] | None = None,
    ylim: tuple[float, float] | None = None,
    title: str | None = None,
    style_origin: bool = False,
    vertical_asymptotes: list[float] | None = None,
    horizontal_asymptotes: list[float] | None = None,
    defined_points: list[tuple[float, float]] | None = None,
    open_points: list[tuple[float, float]] | None = None,
    emphasized_open_points: list[tuple[float, float]] | None = None,
    labeled_points: list[tuple[float, float, str]] | None = None,
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Plot expressions over open or closed intervals."""

    if num < 2:
        raise ValueError("num must be at least 2")
    variable = var or sp.symbols("x")
    xlim = xlim or (-5, 5)
    ylim = ylim or (-5, 5)
    if xlim[0] >= xlim[1] or ylim[0] >= ylim[1]:
        raise ValueError("xlim and ylim must be increasing intervals")

    piece_list = list(pieces)
    if not piece_list:
        raise ValueError("pieces must not be empty")

    if ax is None:
        _, ax = plt.subplots(figsize=(6.5, 6.5))

    if not style_origin:
        ax.axhline(0, linewidth=1.4)
        ax.axvline(0, linewidth=1.4)

    for expression, (start, end, left_closed, right_closed) in piece_list:
        if start >= end:
            raise ValueError(f"piece interval must be increasing: {(start, end)}")
        function = sp.lambdify(variable, expression, "numpy")
        step = (end - start) / max(num - 1, 1)
        interior_start = start if left_closed else start + step
        interior_end = end if right_closed else end - step
        if interior_start > interior_end:
            interior_start, interior_end = start, end

        x_values = np.linspace(interior_start, interior_end, num)
        with np.errstate(all="ignore"):
            y_values = np.asarray(function(x_values), dtype=float)
        if y_values.shape == ():
            y_values = np.full_like(x_values, y_values, dtype=float)
        finite = np.isfinite(y_values)
        ax.plot(x_values[finite], y_values[finite], linewidth=2)

        for x_value, is_closed in ((start, left_closed), (end, right_closed)):
            with np.errstate(all="ignore"):
                y_value = function(x_value)
            if np.isfinite(y_value):
                ax.plot(
                    x_value,
                    y_value,
                    marker="o",
                    markerfacecolor="black" if is_closed else "white",
                    markeredgecolor="black",
                    markersize=7,
                    zorder=6,
                )

    if title:
        ax.set_title(title)
    if style_origin:
        style_axes_origin_with_arrows(ax, xlim, ylim, grid=False)
    else:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)

    for collection, size, edge_width in (
        (open_points or [], 8, 1),
        (emphasized_open_points or [], 14, 2),
    ):
        for x_value, y_value in collection:
            ax.plot(
                x_value,
                y_value,
                marker="o",
                markerfacecolor="white",
                markeredgecolor="black",
                markeredgewidth=edge_width,
                markersize=size,
                zorder=7,
            )

    for x_value, y_value in defined_points or []:
        ax.plot(x_value, y_value, marker="o", markersize=6, color="black", zorder=8)

    for x_value, y_value, label in labeled_points or []:
        ax.plot(x_value, y_value, marker="o", markersize=6, color="black", zorder=8)
        dx = 0.05 * (xlim[1] - xlim[0])
        dy = 0.05 * (ylim[1] - ylim[0])
        x_text = x_value - dx if x_value < 0 else x_value + dx
        ax.text(
            x_text,
            y_value - dy,
            rf"${label}$",
            fontsize=8,
            ha="right" if x_value < 0 else "left",
            va="top",
        )

    trig_domain = np.isclose(xlim[1] - xlim[0], 2 * np.pi, atol=1e-2)
    if not trig_domain:
        x_spacing = _major_spacing(xlim[1] - xlim[0])
        y_spacing = _major_spacing(ylim[1] - ylim[0])
        if ylim[0] >= 1000:
            y_spacing = max(y_spacing, 50)
        ax.set_xticks(np.arange(xlim[0], xlim[1] + x_spacing, x_spacing))
        ax.set_yticks(np.arange(ylim[0], ylim[1] + y_spacing, y_spacing))
        ax.set_xticks(
            np.arange(xlim[0], xlim[1] + x_spacing / 2, x_spacing / 2),
            minor=True,
        )
        ax.set_yticks(
            np.arange(ylim[0], ylim[1] + y_spacing / 2, y_spacing / 2),
            minor=True,
        )
    else:
        ax.set_xticks([], minor=True)

    ax.grid(True, which="major", linewidth=0.8, alpha=0.35)
    ax.grid(True, which="minor", linewidth=0.4, alpha=0.20)
    if xlim[1] - xlim[0] <= 2:
        ax.grid(False, which="minor")

    for x_value in vertical_asymptotes or []:
        ax.axvline(x_value, linestyle="--", linewidth=1.4, color="gray")
        ax.text(
            x_value + 0.03 * (xlim[1] - xlim[0]),
            ylim[1] - 0.08 * (ylim[1] - ylim[0]),
            rf"$x={x_value}$",
            color="gray",
            ha="left",
            va="top",
        )

    for y_value in horizontal_asymptotes or []:
        ax.axhline(y_value, linestyle="--", linewidth=1.4, color="gray")
        ax.text(
            xlim[0] + 0.03 * (xlim[1] - xlim[0]),
            y_value + 0.03 * (ylim[1] - ylim[0]),
            rf"$y={y_value}$",
            color="gray",
            ha="left",
            va="bottom",
        )

    if show:
        plt.show()
    return ax
