"""Regression tests for notebook PDF MathJax compatibility."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import nbformat
import pytest

from coursework_math.notebooks.export import (
    _run_nbconvert,
    normalize_math_latex,
    sanitize_notebook,
)


def test_normalizes_nested_mathjax_strikethrough() -> None:
    original = r"$$-\enclose{updiagonalstrike}{\frac{1}{\sqrt{5}}}$$"
    assert normalize_math_latex(original) == r"$$-\cancel{\frac{1}{\sqrt{5}}}$$"


def test_keeps_unrelated_latex_and_other_enclose_commands() -> None:
    original = r"$\frac{1}{2}$ and $\enclose{box}{x}$"
    assert normalize_math_latex(original) == original


def test_sanitization_preserves_original_notebook() -> None:
    markdown = nbformat.v4.new_markdown_cell(
        r"$\enclose{updiagonalstrike}{\frac{1}{\sqrt{5}}}$"
    )
    code = nbformat.v4.new_code_cell("print('unchanged')")
    code.outputs = [
        nbformat.v4.new_output(
            "display_data",
            data={"text/latex": r"$\enclose{updiagonalstrike}{x}$"},
        )
    ]
    notebook = nbformat.v4.new_notebook(cells=[markdown, code])
    before = deepcopy(notebook)

    cleaned = sanitize_notebook(notebook)

    assert notebook == before
    assert cleaned.cells[0].source == r"$\cancel{\frac{1}{\sqrt{5}}}$"
    assert cleaned.cells[1].source == code.source
    assert cleaned.cells[1].outputs[0].data["text/latex"] == r"$\cancel{x}$"


def test_nbconvert_uses_packaged_cancel_template(monkeypatch, tmp_path: Path) -> None:
    commands = []

    def fake_run(command, **kwargs):
        commands.append(command)
        return SimpleNamespace(stdout="", stderr="", returncode=0)

    monkeypatch.setattr("coursework_math.notebooks.export.subprocess.run", fake_run)
    _run_nbconvert(
        tmp_path / "example.ipynb",
        output_dir=tmp_path,
        output_basename="example",
        hide_input=True,
    )

    command = commands[0]
    assert command[command.index("--template") + 1] == "coursework_pdf"
    option = next(
        item for item in command if item.startswith("--TemplateExporter.extra_template_basedirs=")
    )
    template_dir = Path(option.split("=", 1)[1])
    assert (template_dir / "coursework_pdf" / "conf.json").is_file()
    template = (template_dir / "coursework_pdf" / "index.tex.j2").read_text()
    assert r"\usepackage{cancel}" in template
    assert "--no-input" in command


def test_nbconvert_surfaces_latex_error(monkeypatch, tmp_path: Path) -> None:
    def fake_run(command, **kwargs):
        return SimpleNamespace(
            stdout="",
            stderr="Other output\n! Undefined control sequence.\nAdditional output",
            returncode=1,
        )

    monkeypatch.setattr("coursework_math.notebooks.export.subprocess.run", fake_run)
    with pytest.raises(RuntimeError, match="Undefined control sequence"):
        _run_nbconvert(
            tmp_path / "example.ipynb",
            output_dir=tmp_path,
            output_basename="example",
            hide_input=True,
        )
