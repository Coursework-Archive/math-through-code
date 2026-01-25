# mylib/plotting.py
from __future__ import annotations

import re
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from typing import Sequence
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

# Allow:
#  - implicit multiplication: 2x -> 2*x, (x+1)(x-1) -> (x+1)*(x-1)
#  - caret as exponent: x^2 -> x**2
_TRANSFORMS = (
    standard_transformations
    + (implicit_multiplication_application, convert_xor)
)

def equation_latex(equation: str) -> str:
    """
    Return a LaTeX string for the equation, e.g. '2xy + 5y^2 = 4' -> r'2 x y + 5 y^{2} = 4'.
    Does NOT include surrounding $...$.
    """
    _, _, _, lhs, rhs = _parse_equation_to_expr(equation)
    return f"{sp.latex(lhs)} = {sp.latex(rhs)}"


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
        colors="#7b6cff",  # soft purple
    )

    ax = plt.gca()

    # ---- Grid lines ----
    ax.grid(
        True,
        which="major",
        linestyle="-",
        linewidth=0.6,
        alpha=0.6,
    )
    ax.minorticks_on()
    ax.grid(
        True,
        which="minor",
        linestyle="--",
        linewidth=0.4,
        alpha=0.4,
    )

    # ---- Axes through origin ----
    if show_axes:
        ax.axhline(0, color="#dddddd", linewidth=1.2)
        ax.axvline(0, color="#dddddd", linewidth=1.2)

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
        ax.axvline(x0, linestyle="--", linewidth=1.0, alpha=0.6)

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
    x: Sequence[float],
    y: Sequence[float],
    *,
    connect: bool = True,
    marker: str = "o",
    title: str | None = None,
    xlabel: str = "x",
    ylabel: str = "y",
    show_grid: bool = True,
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
        plt.plot(x, y, marker=marker)
    else:
        plt.scatter(x, y)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if title:
        plt.title(title)

    if show_grid:
        plt.grid(True)

    plt.show()
