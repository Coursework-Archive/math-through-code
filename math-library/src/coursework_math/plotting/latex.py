"""LaTeX conversion and notebook display helpers."""

from __future__ import annotations

import re

import sympy as sp

from .parsing import parse_equation


def equation_latex(equation: str) -> str:
    """Return a LaTeX equation string without surrounding dollar signs."""

    parsed = parse_equation(equation)
    lhs = parsed.display_lhs or sp.latex(parsed.lhs)
    return f"{lhs} = {sp.latex(parsed.rhs)}"


def label_latex(equation: str) -> str:
    """Convert common plain-text notation for a compact plot label."""

    value = equation.strip()
    value = re.sub(r"\^\{([^{}]+)\}", r"^{\1}", value)
    value = re.sub(r"\^(-?\d+(?:\.\d+)?)", r"^{\1}", value)
    value = re.sub(r"(?<=\d)(?=[A-Za-z])", r"\\,", value)
    return value


def display_latex(latex: str) -> None:
    """Display raw LaTeX in a Jupyter/IPython environment."""

    try:
        from IPython.display import Math, display
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "display_latex() requires IPython. Install coursework-math[notebook]."
        ) from exc

    display(Math(latex))


def display_equation(equation: str) -> None:
    """Parse and display an equation in a Jupyter/IPython environment."""

    display_latex(equation_latex(equation))
