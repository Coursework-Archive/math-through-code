"""Explicit and implicit equation plotting."""

from __future__ import annotations

import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from .axes import (
    AXIS_COLOR,
    GRID_MAJOR_ALPHA,
    GRID_MINOR_ALPHA,
    PRIMARY_LINE_COLOR,
)
from .parsing import ParsedEquation, parse_equation


def _discontinuities(
    parsed: ParsedEquation,
    *,
    tolerance: float,
) -> tuple[list[tuple[float, float]], list[float], list[sp.Expr]]:
    lhs, rhs, x, y = parsed.lhs, parsed.rhs, parsed.x, parsed.y
    holes: list[tuple[float, float]] = []
    asymptotes: list[float] = []
    excluded: list[sp.Expr] = []

    if lhs == y and y not in rhs.free_symbols:
        rational = sp.together(rhs)
        numerator = sp.factor(sp.numer(rational))
        denominator = sp.factor(sp.denom(rational))
        if denominator == 1 or y in denominator.free_symbols:
            return holes, asymptotes, excluded

        excluded = sp.solve(sp.Eq(denominator, 0), x)
        common_factor = sp.factor(sp.gcd(numerator, denominator))
        hole_values: set[float] = set()
        if common_factor != 1:
            for x_value in sp.solve(sp.Eq(common_factor, 0), x):
                y_value = sp.limit(rational, x, x_value)
                if y_value.is_real and y_value.is_finite:
                    x_float = float(x_value)
                    holes.append((x_float, float(y_value)))
                    hole_values.add(x_float)

        for x_value in excluded:
            try:
                x_float = float(x_value)
            except (TypeError, ValueError):
                continue
            if not any(abs(x_float - hole) <= tolerance for hole in hole_values):
                asymptotes.append(x_float)
        return holes, asymptotes, excluded

    expression = sp.together(lhs) - sp.together(rhs)
    denominator = sp.factor(sp.denom(sp.together(expression)))
    if denominator != 1 and y not in denominator.free_symbols:
        excluded = sp.solve(sp.Eq(denominator, 0), x)
    return holes, asymptotes, excluded


def plot_equation(
    equation: str,
    exclude: str | None = None,
    xlim: tuple[float, float] = (-5, 5),
    ylim: tuple[float, float] = (-5, 5),
    grid: int = 600,
    title: str | None = None,
    show_axes: bool = True,
    display_latex: bool = False,
    latex_title: bool = True,
    auto_exclude: bool = True,
    tol: float = 1e-3,
    *,
    ax: matplotlib.axes.Axes | None = None,
    show: bool = True,
) -> matplotlib.axes.Axes:
    """Plot an explicit or implicit equation from a string."""

    if grid < 50:
        raise ValueError("grid must be at least 50")
    if xlim[0] >= xlim[1] or ylim[0] >= ylim[1]:
        raise ValueError("xlim and ylim must be increasing intervals")

    parsed = parse_equation(equation)
    holes: list[tuple[float, float]] = []
    asymptotes: list[float] = []
    excluded_values: list[sp.Expr] = []

    if auto_exclude:
        holes, asymptotes, excluded_values = _discontinuities(parsed, tolerance=tol)
        if exclude is None and excluded_values:
            exclude = " | ".join(
                f"Abs({parsed.x} - ({sp.sstr(value)})) < {tol}"
                for value in excluded_values
            )

    if display_latex:
        try:
            from IPython.display import Math, display
        except ImportError:  # pragma: no cover - environment dependent
            pass
        else:
            lhs = parsed.display_lhs or sp.latex(parsed.lhs)
            display(Math(rf"{lhs} = {sp.latex(parsed.rhs)}"))

    function = sp.lambdify((parsed.x, parsed.y), parsed.expression, modules=["numpy"])
    x_values = np.linspace(xlim[0], xlim[1], grid)
    y_values = np.linspace(ylim[0], ylim[1], grid)
    x_mesh, y_mesh = np.meshgrid(x_values, y_values)

    with np.errstate(all="ignore"):
        z_values = function(x_mesh, y_mesh)

    z_values = np.asarray(z_values)
    if z_values.shape == ():
        z_values = np.full_like(x_mesh, z_values, dtype=float)

    if exclude:
        exclude_expression = sp.sympify(
            exclude,
            locals={str(parsed.x): parsed.x, str(parsed.y): parsed.y, "Abs": sp.Abs},
        )
        exclude_function = sp.lambdify(
            (parsed.x, parsed.y),
            exclude_expression,
            modules=["numpy"],
        )
        with np.errstate(all="ignore"):
            mask = exclude_function(x_mesh, y_mesh)
        z_values = np.ma.masked_where(mask, z_values)

    if ax is None:
        _, ax = plt.subplots(figsize=(6, 6))

    ax.contour(
        x_mesh,
        y_mesh,
        z_values,
        levels=[0],
        linewidths=2.0,
        colors=PRIMARY_LINE_COLOR,
    )
    ax.grid(True, which="major", linestyle="-", linewidth=0.6, alpha=GRID_MAJOR_ALPHA)
    ax.minorticks_on()
    ax.grid(True, which="minor", linestyle="--", linewidth=0.4, alpha=GRID_MINOR_ALPHA)

    if show_axes:
        ax.axhline(0, color=AXIS_COLOR, linewidth=1.2)
        ax.axvline(0, color=AXIS_COLOR, linewidth=1.2)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel(str(parsed.x))
    ax.set_ylabel(str(parsed.y))

    for x_value, y_value in holes:
        ax.plot(
            x_value,
            y_value,
            marker="o",
            markersize=9,
            markerfacecolor="none",
            markeredgewidth=2,
        )

    for x_value in asymptotes:
        ax.axvline(x_value, linestyle="--", linewidth=1.0, alpha=GRID_MAJOR_ALPHA)

    if not display_latex:
        if title:
            ax.set_title(title, pad=12)
        elif latex_title:
            lhs = parsed.display_lhs or sp.latex(parsed.lhs)
            ax.set_title(rf"${lhs} = {sp.latex(parsed.rhs)}$", fontsize=12, pad=12)

    if show:
        plt.show()
    return ax
