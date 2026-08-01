# mylib/plotting.py
from __future__ import annotations

import re
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from typing import Sequence
from typing import Iterable, Tuple, List, Optional
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)
Point = Tuple[float, float]

# Allow:
#  - implicit multiplication: 2x -> 2*x, (x+1)(x-1) -> (x+1)*(x-1)
#  - caret as exponent: x^2 -> x**2
_TRANSFORMS = (
    standard_transformations
    + (implicit_multiplication_application, convert_xor)
)

# ---- Plot styling defaults ----

PRIMARY_LINE_COLOR = "#7b6cff"   # soft purple
AXIS_COLOR = "#dddddd"
GRID_MAJOR_ALPHA = 0.6
GRID_MINOR_ALPHA = 0.4

def equation_latex(equation: str) -> str:
    """
    Return a LaTeX string for the equation.
    Does NOT include surrounding $...$.
    """
    parsed = _parse_equation_to_expr(equation)

    # Supports both old (5-tuple) and new (6-tuple) return shapes
    lhs = parsed[3]
    rhs = parsed[4]

    return f"{sp.latex(lhs)} = {sp.latex(rhs)}"

# def equation_latex(equation: str) -> str:
#     """
#     Return a LaTeX string for the equation, e.g. '2xy + 5y^2 = 4' -> r'2 x y + 5 y^{2} = 4'.
#     Does NOT include surrounding $...$.
#     """
#     _, _, _, lhs, rhs = _parse_equation_to_expr(equation)
#     return f"{sp.latex(lhs)} = {sp.latex(rhs)}"


def display_latex(latex: str) -> None:
    """
    Display raw LaTeX in a Jupyter notebook (no parsing).
    The string should NOT include surrounding $...$.
    """
    try:
        from IPython.display import display, Math
    except ImportError as e:
        raise RuntimeError(
            "display_equation() requires a Jupyter/IPython environment."
        ) from e

    display(Math(latex))



def display_equation(equation: str) -> None:
    """
    Display the equation as LaTeX in a Jupyter notebook.
    Safe to import in non-notebook contexts (will raise a friendly error if IPython isn't available).
    """
    latex_str = equation_latex(equation)
    try:
        from IPython.display import display, Math  # imported only when needed
    except ImportError as e:
        raise RuntimeError(
            "display_equation() requires a Jupyter/IPython environment. "
            "Use equation_latex() instead, or call plot_equation(..., latex_title=True)."
        ) from e

    display(Math(latex_str))

def label_latex(equation: str) -> str:
    """
    Lightweight LaTeX for labels/titles. Preserves function parentheses like f(x).
    Does NOT attempt full symbolic parsing.
    Returns a string WITHOUT surrounding $...$.
    """
    s = equation.strip()

    # Convert ^ to exponent for LaTeX (optional)
    s = s.replace("^", "^{")  # we'll close braces below carefully (see note)

    # Better: handle simple x^2 patterns safely:
    s = re.sub(r"\^(\d+)", r"^{\1}", s)

    # Add thin space between a number and a variable: 2x -> 2\,x
    s = re.sub(r"(\d)([A-Za-z])", r"\1\\,\2", s)

    # Keep function calls intact: f(x) stays f(x)
    # (no change needed)

    return s


def set_pi_ticks(ax):
    ticks = np.array([
        -np.pi,
        -np.pi/2,
        0,
        np.pi/2,
        np.pi
    ])

    labels = [
        r"$-\pi$",
        r"$-\frac{\pi}{2}$",
        r"$0$",
        r"$\frac{\pi}{2}$",
        r"$\pi$"
    ]

    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)


def _parse_equation_to_expr(
    equation: str,
    x_symbol: str = "x",
    y_symbol: str = "y",
    display_lhs: str | None = None,
):
    """
    Converts an equation string into F(x,y)=0 for contour plotting.
    Now supports function-style LHS like:
      "f(x) = (x^2-4)/(x-2)"
      "g(t) = sqrt(3-t) - sqrt(2+t)"
    by interpreting it as:
      y = RHS   with independent variable inferred from parentheses.
    """
    eq = equation.strip()

    # --- Detect "name(var) = ..." on the LHS (e.g., f(x)=..., g(t)=...) ---
    # Captures: func_name, var_name
    m = re.match(r"^\s*([A-Za-z]\w*)\s*\(\s*([A-Za-z]\w*)\s*\)\s*(==|=)\s*(.+)$", eq)
    if m:
        func_name, var_name, _eqsign, rhs_only = m.groups()
        x_symbol = var_name
        display_lhs = f"{func_name}({var_name})"
        eq = f"{y_symbol} = {rhs_only}"

    # Now create symbols using (possibly updated) x_symbol
    x, y = sp.symbols(f"{x_symbol} {y_symbol}", real=True)
    local = {x_symbol: x, y_symbol: y}

    # Split equation
    if "==" in eq:
        lhs_str, rhs_str = eq.split("==", 1)
    elif "=" in eq:
        lhs_str, rhs_str = eq.split("=", 1)
    else:
        # Expression only:
        expr = parse_expr(eq, local_dict=local, transformations=_TRANSFORMS)
        if y in expr.free_symbols:
            lhs, rhs = expr, sp.Integer(0)
        else:
            lhs, rhs = y, expr
        F = sp.simplify(lhs - rhs)
        return F, x, y, lhs, rhs

    lhs = parse_expr(lhs_str, local_dict=local, transformations=_TRANSFORMS)
    rhs = parse_expr(rhs_str, local_dict=local, transformations=_TRANSFORMS)
    F = sp.simplify(lhs - rhs)
    return F, x, y, lhs, rhs, display_lhs

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
) -> None:
    """
    Plots an implicit equation given as a string, e.g.:
      plot_equation("2xy + 5y^2 = 4")

    Produces the curve where F(x,y)=0 using a contour plot.
    """
    F, x, y, lhs, rhs, display_lhs = _parse_equation_to_expr(equation)

    holes: list[tuple[float, float]] = []
    asymptotes: list[float] = []
    bad_x: list[sp.Expr] = []
    den = sp.Integer(1)

    # --- Detect denominator + excluded x-values (only if safe) ---
    bad_x: list[sp.Expr] = []
    den = sp.Integer(1)

    if auto_exclude:
        if lhs == y and (y not in rhs.free_symbols):
            # FUNCTION GRAPH: y = f(x)
            rat = sp.together(rhs)
            num = sp.factor(sp.numer(rat))
            den = sp.factor(sp.denom(rat))

            if den != 1 and (y not in den.free_symbols):
                bad_x = sp.solve(sp.Eq(den, 0), x)

                # classify discontinuities: hole if factor cancels
                g = sp.factor(sp.gcd(num, den))

                hole_xs = []
                if g != 1:
                    hole_xs = sp.solve(sp.Eq(g, 0), x)
                    for x0 in hole_xs:
                        y0 = sp.limit(rat, x, x0)
                        if y0.is_real and y0.is_finite:
                            holes.append((float(x0), float(y0)))

                hole_x_set = {hx for hx, _ in holes}
                for x0 in bad_x:
                    try:
                        x0f = float(x0)
                        if x0f not in hole_x_set:
                            asymptotes.append(x0f)
                    except Exception:
                        pass

                if exclude is None and bad_x:
                    exclude = " | ".join([f"Abs(x - ({sp.sstr(v)})) < {tol}" for v in bad_x])

        else:
            # IMPLICIT EQUATION
            expr_for_denoms = sp.together(lhs) - sp.together(rhs)
            den = sp.factor(sp.denom(sp.together(expr_for_denoms)))

            if den != 1 and (y not in den.free_symbols):
                bad_x = sp.solve(sp.Eq(den, 0), x)
                if exclude is None and bad_x:
                    exclude = " | ".join([f"Abs(x - ({sp.sstr(v)})) < {tol}" for v in bad_x])

    # Optional notebook LaTeX display
    if display_latex:
        try:
            from IPython.display import display, Math
            if display_lhs is not None:
                display(Math(rf"{display_lhs} = {sp.latex(rhs)}"))
            else:
                display(Math(f"{sp.latex(lhs)} = {sp.latex(rhs)}"))
        except ImportError:
            pass

    f_num = sp.lambdify((x, y), F, modules=["numpy"])

    xs = np.linspace(xlim[0], xlim[1], grid)
    ys = np.linspace(ylim[0], ylim[1], grid)
    X, Y = np.meshgrid(xs, ys)

    with np.errstate(all="ignore"):
        Z = f_num(X, Y)

    # Apply exclusion mask AFTER X,Y,Z exist
    if exclude:
        exclude_expr = sp.sympify(exclude)
        exclude_fn = sp.lambdify((x, y), exclude_expr, modules=["numpy"])
        with np.errstate(all="ignore"):
            mask = exclude_fn(X, Y)
        Z = np.ma.masked_where(mask, Z)

    plt.figure(figsize=(6, 6))

    # ---- Curve (thicker, cleaner) ----
    plt.contour(
        X,
        Y,
        Z,
        levels=[0],
        linewidths=2.0,
        colors=PRIMARY_LINE_COLOR,
    )

    ax = plt.gca()

    # ---- Grid lines ----
    ax.grid(
        True,
        which="major",
        linestyle="-",
        linewidth=0.6,
        alpha=GRID_MAJOR_ALPHA,
    )
    ax.minorticks_on()
    ax.grid(
        True,
        which="minor",
        linestyle="--",
        linewidth=0.4,
        alpha=GRID_MINOR_ALPHA,
    )

    # ---- Axes through origin ----
    if show_axes:
        ax.axhline(0, color=AXIS_COLOR, linewidth=1.2)
        ax.axvline(0, color=AXIS_COLOR, linewidth=1.2)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_xlabel(str(x))
    ax.set_ylabel(str(y))

    # Mark holes as open circles
    for x0, y0 in holes:
        ax.plot(
            x0, y0,
            marker="o",
            markersize=9,
            markerfacecolor="none",
            markeredgewidth=2
        )

    # Optional: draw vertical asymptotes (dashed)
    for x0 in asymptotes:
        ax.axvline(x0, linestyle="--", linewidth=1.0, alpha=GRID_MAJOR_ALPHA)

    # ---- Title logic (this is the key part) ----
    if not display_latex:
        if title:
            ax.set_title(title, pad=12)
        elif latex_title:
            if display_lhs is not None:
                ax.set_title(
                    rf"${display_lhs} = {sp.latex(rhs)}$",
                    fontsize=12,
                    pad=12
                )
            else:
                ax.set_title(
                    f"${sp.latex(lhs)} = {sp.latex(rhs)}$",
                    fontsize=12,
                    pad=12
                )

    plt.show()


def plot_data_points(
    x, y,
    *,
    connect=True,
    marker="o",
    title=None,
    xlabel="x",
    ylabel="y",
    show_grid=True,
    tangent=False,
    tangent_x0=None,
    tangent_y0=None,
    tangent_slope=None,
) -> None:
    """
    Plot discrete data points, optionally connected by line segments.

    Parameters
    ----------
    x, y : sequences of numbers
        Data coordinates.
    connect : bool
        Whether to connect points with line segments.
    marker : str
        Marker style for points.
    title : str | None
        Optional plot title.
    xlabel, ylabel : str
        Axis labels.
    show_grid : bool
        Whether to show grid lines.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    if connect:
        (line,) = plt.plot(x, y, marker=marker, color="black", label="s(t)")

    else:
        plt.scatter(x, y)

    if tangent:
        tangent_color = "red"

        xt = [tangent_x0 - 1, tangent_x0 + 1]
        yt = [tangent_y0 + tangent_slope * (x - tangent_x0) for x in xt]

        # tangent line
        plt.plot(
            xt,
            yt,
            linestyle="--",
            color=tangent_color,
            linewidth=2,
            label="Tangent line"
        )

        # tangent points
        plt.scatter(
            xt,
            yt,
            color=tangent_color,
            s=70,
            zorder=5
        )

        # labels for tangent points
        for xi, yi in zip(xt, yt):
            # Put the left point label BELOW the line, right point label ABOVE the line
            dx, dy = (8, -14) if xi < tangent_x0 else (8, 8)

            plt.annotate(
                f"({xi:.1f}, {yi:.1f})",
                xy=(xi, yi),
                xytext=(dx, dy),
                textcoords="offset points",
                color=tangent_color,
                fontsize=9,
                ha="left",
                va="bottom" if dy > 0 else "top",
                zorder=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="black", ec="none", alpha=0.6),
            )


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if title:
        plt.title(title)

    if show_grid:
        plt.grid(True)

    plt.show()


def transform_points(points: Iterable[Point],
                     *,
                     x_mult: float = 1.0,
                     x_negate: bool = False,
                     y_mult: float = 1.0,
                     y_negate: bool = False) -> List[Point]:
    out: List[Point] = []
    """
    Transform points for horizontal transformations of the form y = f(kx) or y = f(-x).

    If y = f(kx), then x_new = x_old / k  -> set x_mult = 1/k.
      - y = f(2x):  x_mult = 1/2
      - y = f((1/2)x): x_mult = 2
    If y = f(-x): x_negate = True

    Notes:
    - This helper changes x only (horizontal transforms). y stays the same.
    """
    for x, y in points:
        xn = -x if x_negate else x
        yn = -y if y_negate else y
        out.append((xn * x_mult, yn * y_mult))
    return out


def plot_polyline(
    points,
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
) -> None:
    x, y = zip(*points)

    plt.figure(figsize=(6.5, 6.5))
    ax = plt.gca()

    # ---- Axes through origin ----
    ax.axhline(0, color=AXIS_COLOR, linewidth=1.6, zorder=0)
    ax.axvline(0, color=AXIS_COLOR, linewidth=1.6, zorder=0)

    # ---- Plot ----
    ax.plot(x, y, marker=marker, color=color, linewidth=2.2)

    # ---- Aspect ----
    ax.set_aspect("equal", adjustable="box")

    # ---- FIXED WINDOW (same size every time) ----
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)

    # ---- LaTeX logic: exactly ONE output path ----
    if equation:
        if display_latex:
            # Notebook LaTeX ABOVE the plot output (your preferred look)
            try:
                from IPython.display import display, Math
                display(Math(equation))  # preserves parentheses exactly
            except ImportError:
                pass

        else:
            # Put label INSIDE the plot at top-left (not a centered title)
            if latex_title:
                latex = label_latex(equation)  # lightweight, keeps f(x)
                loc_map = {
                    "tl": (latex_pad, 1 - latex_pad, "left", "top"),
                    "tr": (1 - latex_pad, 1 - latex_pad, "right", "top"),
                    "bl": (latex_pad, latex_pad, "left", "bottom"),
                    "br": (1 - latex_pad, latex_pad, "right", "bottom"),
                }
                if latex_loc not in loc_map:
                    raise ValueError("latex_loc must be one of: 'tl', 'tr', 'bl', 'br'")

                xx, yy, ha, va = loc_map[latex_loc]
                ax.text(
                    xx, yy, rf"${latex}$",
                    transform=ax.transAxes,
                    ha=ha, va=va,
                    fontsize=latex_fontsize,
                )
            else:
                # Plain text label, same placement
                ax.text(
                    latex_pad, 1 - latex_pad, equation,
                    transform=ax.transAxes,
                    ha="left", va="top",
                    fontsize=latex_fontsize,
                )

    ax.set_xticks(np.arange(xlim[0], xlim[1] + 0.5, 0.5), minor=True)
    ax.set_yticks(np.arange(ylim[0], ylim[1] + 0.5, 0.5), minor=True)
    ax.grid(True, which="minor", linestyle="--", linewidth=0.4, alpha=0.4)
    plt.show()





Interval = Tuple[float, float, bool, bool]
# (x_start, x_end, left_closed, right_closed)
def plot_piecewise(
    pieces: Iterable[tuple[sp.Expr, Interval]],
    *,
    var: sp.Symbol = sp.symbols("x"),
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
    labeled_points: list[tuple[float, float, str]] | None = None
) -> None:
    """
    Plot a piecewise-defined function.

    pieces:
        Iterable of (expression, interval)
        interval = (x_start, x_end, left_closed, right_closed)

    Example interval:
        (-2, 1, True, False)  ->  [-2, 1)
    """

    plt.figure(figsize=(6.5, 6.5))
    ax = plt.gca()

    # (Optional) keep these if you like; style_origin will visually replace them anyway
    if not style_origin:
        ax.axhline(0, linewidth=1.4)
        ax.axvline(0, linewidth=1.4)

    drawn_open_points = set()
    for expr, (a, b, left_closed, right_closed) in pieces:
        f = sp.lambdify(var, expr, "numpy")
        dx = (b - a) / max(num - 1, 1)
        a_in = a + dx
        b_in = b - dx

        if a_in >= b_in:
            a_in = a
            b_in = b

        xs = np.linspace(a_in, b_in, num)

        with np.errstate(all="ignore"):
            ys = f(xs)

        ys = np.asarray(ys, dtype=float)
        # If lambdify returned a scalar (e.g., constant function), broadcast to xs
        if ys.shape == ():
            ys = np.full_like(xs, ys, dtype=float)
        mask = np.isfinite(ys)

        ax.plot(xs[mask], ys[mask], color="black", linewidth=2)

        # Endpoints (only evaluate if we will plot them)
        # left endpoint marker
        if left_closed:
            with np.errstate(all="ignore"):
                ya = f(a)
            if np.isfinite(ya):
                ax.plot(a, ya, "o", color="black")

        # right endpoint marker
        if right_closed:
            with np.errstate(all="ignore"):
                yb = f(b)
            if np.isfinite(yb):
                ax.plot(b, yb, "o", color="black")

    if title:
        ax.set_title(title)

    # ---- Final plot formatting (limits, aspect, ticks, grid) ----
    if xlim is None:
        xlim = (-5, 5)
    if ylim is None:
        ylim = (-5, 5)

    ax.set_aspect("auto")

    # If you want axes through origin with arrows, do it FIRST (it sets limits/spines)
    if style_origin:
        style_axes_origin_with_arrows(ax, xlim, ylim, grid=False)
    else:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)

    # ---- Explicit points ----
    if open_points:
        for x0, y0 in open_points:
            ax.plot(x0, y0, "o",
                    markerfacecolor="white",
                    markeredgecolor="black",
                    markersize=8,
                    zorder=6)

    # emphasized open holes (shared endpoints)
    if emphasized_open_points:
        for x0, y0 in emphasized_open_points:
            ax.plot(x0, y0, "o",
                    markerfacecolor="white",
                    markeredgecolor="black",
                    markeredgewidth=2,
                    markersize=14,
                    zorder=6)

    if defined_points:
        for x0, y0 in defined_points:
            ax.plot(x0, y0, marker="o", markersize=6,
                    color="black", zorder=7)

    # ---- Labeled points (LaTeX support) ----
    if labeled_points:
        for x0, y0, label in labeled_points:
            ax.plot(x0, y0, marker="o", markersize=6,
                    color="black", zorder=8)

            dx = 0.05 * (xlim[1] - xlim[0])
            dy = 0.05 * (ylim[1] - ylim[0])

            # If point is on left side, shift left
            if x0 < 0:
                x_text = x0 - dx
                ha_align = 'right'
            else:
                x_text = x0 + dx
                ha_align = 'left'

            ax.text(
                x_text,
                y0 - dy,
                rf"${label}$",
                fontsize=8,
                ha=ha_align,
                va='top'
            )

    # ---- Major + minor ticks (smaller grid sections) ----
    is_trig = np.isclose(xlim[1] - xlim[0], 2 * np.pi, atol=1e-2)

    if not is_trig:
        x_span = xlim[1] - xlim[0]
        y_span = ylim[1] - ylim[0]

        # Adaptive major spacing
        if x_span > 100:
            x_major = 20
        elif x_span > 50:
            x_major = 10
        elif x_span > 20:
            x_major = 5

        if y_span > 20:
            y_major = 5
        elif y_span > 8:
            y_major = 1
        else:
            y_major = y_span / 6

        # Only for big-number graphs: ensure labels aren't too dense / weird
        if ylim[0] >= 1000:
            y_major = max(y_major, 50)

        ax.set_xticks(np.arange(xlim[0], xlim[1] + x_major, x_major))
        ax.set_yticks(np.arange(ylim[0], ylim[1] + y_major, y_major))

        ax.set_xticks(np.arange(xlim[0], xlim[1] + x_major / 2, x_major / 2), minor=True)
        ax.set_yticks(np.arange(ylim[0], ylim[1] + y_major / 2, y_major / 2), minor=True)

    else:
        # keep π ticks that were set in style_axes_origin_with_arrows
        ax.set_xticks([], minor=True)
        # (optional) you can still set y ticks adaptively if you want, but not required


    # ---- Grid styling ----
    ax.grid(True, which="major", linewidth=0.8, alpha=0.35)
    ax.grid(True, which="minor", linewidth=0.4, alpha=0.20)

    x_span = xlim[1] - xlim[0]
    if x_span <= 2:
        ax.grid(False, which="minor")  # keep minor ticks, hide minor grid

    # ---- Asymptotes ----
    if vertical_asymptotes:
        for x0 in vertical_asymptotes:
            ax.axvline(x0, linestyle="--", linewidth=1.4, color="gray")
            ax.text(
                x0 + 0.03 * (xlim[1] - xlim[0]),
                ylim[1] - 0.08 * (ylim[1] - ylim[0]),
                rf"$x={x0}$",
                color="gray",
                ha="left",
                va="top",
            )

    if horizontal_asymptotes:
        for y0 in horizontal_asymptotes:
            ax.axhline(y0, linestyle="--", linewidth=1.4, color="gray")
            ax.text(
                xlim[0] + 0.03 * (xlim[1] - xlim[0]),
                y0 + 0.03 * (ylim[1] - ylim[0]),
                rf"$y={y0}$",
                color="gray",
                ha="left",
                va="bottom",
            )

    plt.show()


def style_axes_origin_with_arrows(ax, xlim, ylim, *, grid=True):
    # Limits first
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    # --- Special π tick formatting if domain is trig-like ---
    if np.isclose(xlim[1] - xlim[0], 2*np.pi, atol=1e-2):
        ticks = np.array([
            -np.pi,
            -np.pi / 2,
            0,
            np.pi / 2,
            np.pi
        ])

        labels = [
            r"$-\pi$",
            r"$-\frac{\pi}{2}$",
            r"$0$",
            r"$\frac{\pi}{2}$",
            r"$\pi$"
        ]

        ax.set_xticks(ticks)
        ax.set_xticklabels(labels)


    # Put axes (spines) through the origin so tick labels sit ON the axes
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    # Make spines visible and black
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    ax.spines["left"].set_linewidth(1.6)
    ax.spines["bottom"].set_linewidth(1.6)

    # Ticks only on these axes
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    # Ensure tick labels show
    ax.tick_params(axis="both", which="both", colors="black", labelsize=10)

    # Grid lines
    if grid:
        ax.grid(True, alpha=0.25, linewidth=1)

    # Arrowheads on +x and +y ends (and optionally -x/-y)
    xr = xlim[1] - xlim[0]
    yr = ylim[1] - ylim[0]

    # +x arrow
    ax.annotate(
        "", xy=(xlim[1], 0), xytext=(xlim[1] - 0.06 * xr, 0),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.6),
        clip_on=False,
    )
    # +y arrow
    ax.annotate(
        "", xy=(0, ylim[1]), xytext=(0, ylim[1] - 0.06 * yr),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.6),
        clip_on=False,
    )

    # Axis labels near arrowheads
    ax.text(xlim[1] - 0.08 * xr, 0 + 0.04 * yr, "x", color="black")
    ax.text(0 + 0.04 * xr, ylim[1] - 0.10 * yr, "y", color="black")


def epsilon_delta_plot(
    f,
    a,
    L,
    eps=0.5,
    delta=0.5,
    xlim=(-5, 5),
    ylim=(-10, 10),
    title="",
):
    xs = np.linspace(*xlim, 1200)
    ys = f(xs)

    fig = plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # ---- Function (black) ----
    ax.plot(xs, ys, color="black", linewidth=2)

    # ---- Axes through origin (black) ----
    style_axes_origin_with_arrows(ax, xlim, ylim, grid=True)

    # ---- ε lines (red), from y-axis to intersection with graph ----
    for y_target in (L + eps, L - eps):
        idx = np.argmin(np.abs(ys - y_target))
        x_hit = xs[idx]
        ax.plot([0, x_hit], [y_target, y_target],
                color="red", linestyle="--", linewidth=1.6)

    # ---- δ lines (red), from x-axis to graph at x=a±δ ----
    for x_delta in (a - delta, a + delta):
        y_hit = f(x_delta)
        ax.plot([x_delta, x_delta], [0, y_hit],
                color="red", linestyle="--", linewidth=1.6)

    # ---- Limits / grid ----
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.grid(False)

    # ---- Ensure x ticks include a-δ, a, a+δ (tick locations won't "move"; we just include them) ----
    base_ticks = list(ax.get_xticks())
    special = [a - delta, a, a + delta]
    xticks = sorted(set([*base_ticks, *special]))
    ax.set_xticks(xticks)

    # ---- δ labels ABOVE the x-axis AND staggered so they don’t overlap ----
    y0 = 0.0
    y_range = (ylim[1] - ylim[0])
    y_text = y0 + 0.03 * y_range      # above the x-axis line

    x_range = (xlim[1] - xlim[0])
    x_stagger = 0.03 * x_range        # horizontal stagger amount

    # Stagger left/center/right labels slightly
    ax.text(a - delta - x_stagger, y_text, "a − δ", ha="center", va="bottom", color="red")
    ax.text(a,                 y_text, "a",     ha="center", va="bottom", color="red")
    ax.text(a + delta + x_stagger, y_text, "a + δ", ha="center", va="bottom", color="red")

    # ---- ε labels (red) ----
    ax.text(xlim[0] + 0.02*x_range, L + eps, "L + ε", va="bottom", color="red")
    ax.text(xlim[0] + 0.02*x_range, L - eps, "L − ε", va="top", color="red")

    # ---- Axis labels “x” and “y” (like textbook) ----
    ax.text(xlim[1] - 0.05*x_range, 0 + 0.02*y_range, "x", color="black")
    ax.text(0 + 0.02*x_range, ylim[1] - 0.05*y_range, "y", color="black")

    # ---- Title ----
    if title:
        ax.set_title(title)

    plt.show()




