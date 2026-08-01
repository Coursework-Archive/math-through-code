"""Internal equation parsing helpers used by plotting and LaTeX modules."""

from __future__ import annotations

import re
from dataclasses import dataclass

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

_TRANSFORMS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)


@dataclass(frozen=True, slots=True)
class ParsedEquation:
    """A normalized equation represented as ``expression = 0``."""

    expression: sp.Expr
    x: sp.Symbol
    y: sp.Symbol
    lhs: sp.Expr
    rhs: sp.Expr
    display_lhs: str | None = None


def parse_equation(
    equation: str,
    *,
    x_symbol: str = "x",
    y_symbol: str = "y",
) -> ParsedEquation:
    """Parse explicit, implicit, function-style, or expression-only input."""

    if not equation or not equation.strip():
        raise ValueError("equation must contain a mathematical expression")

    normalized = equation.strip()
    display_lhs: str | None = None

    function_match = re.match(
        r"^\s*([A-Za-z]\w*)\s*\(\s*([A-Za-z]\w*)\s*\)\s*(?:==|=)\s*(.+)$",
        normalized,
    )
    if function_match:
        function_name, variable_name, rhs_only = function_match.groups()
        x_symbol = variable_name
        display_lhs = f"{function_name}({variable_name})"
        normalized = f"{y_symbol}={rhs_only}"

    x, y = sp.symbols(f"{x_symbol} {y_symbol}", real=True)
    local_dict = {x_symbol: x, y_symbol: y}

    if "==" in normalized:
        lhs_text, rhs_text = normalized.split("==", 1)
    elif "=" in normalized:
        lhs_text, rhs_text = normalized.split("=", 1)
    else:
        value = parse_expr(
            normalized,
            local_dict=local_dict,
            transformations=_TRANSFORMS,
        )
        if y in value.free_symbols:
            lhs, rhs = value, sp.Integer(0)
        else:
            lhs, rhs = y, value
        return ParsedEquation(
            expression=sp.simplify(lhs - rhs),
            x=x,
            y=y,
            lhs=lhs,
            rhs=rhs,
            display_lhs=display_lhs,
        )

    lhs = parse_expr(
        lhs_text,
        local_dict=local_dict,
        transformations=_TRANSFORMS,
    )
    rhs = parse_expr(
        rhs_text,
        local_dict=local_dict,
        transformations=_TRANSFORMS,
    )
    return ParsedEquation(
        expression=sp.simplify(lhs - rhs),
        x=x,
        y=y,
        lhs=lhs,
        rhs=rhs,
        display_lhs=display_lhs,
    )
