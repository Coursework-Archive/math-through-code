# Coursework Math Library

Reusable mathematics utilities and a shared knowledge base for Calculus II and future mathematics repositories.

This directory is intentionally separated into two parts:

1. **`knowledge/`** contains reusable Markdown references and supporting images.
2. **`src/coursework_math/`** contains installable Python code that other repositories can import.

Course-specific assignments, exam preparation, grades, and reflections remain in their individual course repositories.

## Project Structure

```text
math-library/
├── knowledge/                    # Reusable Markdown knowledge base
│   ├── README.md
│   ├── images/
│   └── *.md
├── src/
│   └── coursework_math/
│       ├── images.py             # Notebook-safe image loading and display
│       ├── notebooks/
│       │   └── export.py         # Notebook sanitization and PDF export
│       └── plotting/
│           ├── axes.py           # Shared axis and tick formatting
│           ├── equations.py      # Explicit and implicit equation plots
│           ├── latex.py          # Equation-to-LaTeX helpers
│           ├── limits.py         # Epsilon-delta visualization
│           ├── parsing.py        # Internal SymPy equation parsing
│           ├── piecewise.py      # Piecewise function plots
│           └── points.py         # Data, polyline, and point transforms
├── tests/
├── image_utils.py                # Temporary compatibility import
├── plotting.py                   # Temporary compatibility import
├── tools/export_nb.py            # Temporary compatibility command
└── pyproject.toml
```

## Install for Local Development

From a separate course repository located beside `math-through-code`:

```powershell
python -m pip install -e "..\math-library[all]"
```

Editable installation means changes made in this library are immediately available to the course repository.

## Install Directly from GitHub

```powershell
python -m pip install "coursework-math[all] @ git+https://github.com/Coursework-Archive/math-through-code.git@main#subdirectory=math-library"
```

For reproducible coursework, replace `main` with a release tag or commit SHA after the library stabilizes.

## Add to Another Project's `pyproject.toml`

A separate course repository can declare the shared library directly:

```toml
[project]
dependencies = [
  "coursework-math[all] @ git+https://github.com/Coursework-Archive/math-through-code.git@main#subdirectory=math-library",
]
```

During active development, the editable local installation is easier because changes are available immediately. Once releases are tagged, course repositories should pin a tag instead of `main`.

## Plotting Usage

```python
from coursework_math.plotting import (
    epsilon_delta_plot,
    plot_equation,
    plot_piecewise,
    plot_polyline,
)

plot_equation("f(x) = (x^2 - 4) / (x - 2)", xlim=(-5, 5), ylim=(-5, 5))
```

All plotting functions return a Matplotlib `Axes` object. They display immediately by default, while `show=False` allows a course notebook to add labels or combine output before displaying.

```python
ax = plot_equation("y = x^2", show=False)
ax.set_title("Quadratic Example")
```

## Image Usage

```python
from coursework_math.images import load_image, show_image

show_image("images/problem_diagram.jpg", width=700)
```

`show_image` corrects EXIF rotation and displays from memory, so it does not leave temporary files behind.

## Notebook PDF Export

After installing the `pdf` or `all` extra:

```powershell
math-notebook-pdf notebooks/module_1/module_1_assignments.ipynb \
  --author "Brittany L. Bales"
```

The exporter:

- removes known nonstandard notebook metadata,
- stores title, author, and date metadata,
- optionally appends the coursework assistance statement,
- exports without code-cell input,
- writes the PDF beside the source notebook unless another output directory is supplied.

PDF generation requires a working LaTeX installation with `xelatex`. That system dependency is separate from the Python package.

The original command remains available during migration:

```powershell
python ../math-through-code/math-library/tools/export_nb.py notebooks/module_1/module_1_assignments.ipynb
```

## Public API

Prefer imports from these stable locations:

```python
from coursework_math.plotting import plot_equation
from coursework_math.images import show_image
from coursework_math.notebooks import export_notebook_pdf
```

Do not import internal modules whose names begin with an underscore.

## Compatibility Policy

The top-level `plotting.py`, `image_utils.py`, and `tools/export_nb.py` files are compatibility wrappers for older Calculus I notebooks. New notebooks should use the `coursework_math` package imports. The wrappers can be removed after older notebooks have been updated and verified.

## Development Checks

From `math-library/`:

```powershell
python -m pip install -e ".[all,dev]"
python -m pytest
python -m ruff check .
```

## Knowledge-Base Rule

Promote material into `knowledge/` only when it is reusable across courses. Keep the following inside the applicable course repository:

- submitted assignments,
- exam-specific study plans,
- instructor feedback,
- grades and transcripts,
- personal reflections,
- course-specific schedules.
