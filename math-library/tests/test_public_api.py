from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

from coursework_math.notebooks import sanitize_notebook, title_from_filename
from coursework_math.plotting import plot_equation, transform_points


def test_transform_points() -> None:
    assert transform_points([(1, 2)], x_mult=0.5, y_negate=True) == [(0.5, -2.0)]


def test_plot_equation_returns_axes() -> None:
    axes = plot_equation("y=x^2", grid=80, show=False)
    assert axes.get_xlabel() == "x"
    assert axes.get_ylabel() == "y"


def test_title_from_filename() -> None:
    assert title_from_filename("module_2_assignments") == "Module 2 Assignments"


def test_sanitize_notebook_removes_nonstandard_output_keys() -> None:
    import nbformat

    cell = nbformat.v4.new_code_cell(source="1 + 1")
    cell.outputs = [
        nbformat.NotebookNode(
            output_type="display_data",
            data={"text/plain": "2"},
            metadata={"jetTransient": True},
            jetTransient=True,
        )
    ]
    notebook = nbformat.NotebookNode(
        nbformat=4,
        nbformat_minor=5,
        metadata={},
        cells=[cell],
    )
    cleaned = sanitize_notebook(notebook)
    output = cleaned.cells[0].outputs[0]
    assert "jetTransient" not in output
    assert "jetTransient" not in output.metadata
