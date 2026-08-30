"""Sanitize Jupyter notebooks and export them to PDF."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import nbformat


BAD_OUTPUT_KEYS = {"jetTransient"}
BAD_CELL_KEYS: set[str] = set()


def format_today() -> str:
    """Return today's date in a human-readable format."""

    return datetime.now().strftime("%B %d, %Y").replace(" 0", " ")


def title_from_filename(base_name: str) -> str:
    """Convert ``module_2_assignments`` to ``Module 2 Assignments``."""

    words = base_name.replace("-", " ").replace("_", " ").split()
    return " ".join(word if word.isdigit() else word.capitalize() for word in words)


def sanitize_notebook(notebook: nbformat.NotebookNode) -> nbformat.NotebookNode:
    """Return a copy with known nonstandard output and cell keys removed."""

    cleaned = deepcopy(notebook)
    for cell in cleaned.get("cells", []):
        for key in list(cell.keys()):
            if key in BAD_CELL_KEYS:
                cell.pop(key, None)

        outputs = cell.get("outputs")
        if not isinstance(outputs, list):
            continue
        for output in outputs:
            if not isinstance(output, dict):
                continue
            for key in BAD_OUTPUT_KEYS:
                output.pop(key, None)
            metadata = output.get("metadata")
            if isinstance(metadata, dict):
                for key in BAD_OUTPUT_KEYS:
                    metadata.pop(key, None)
    return cleaned


def _run_nbconvert(
    notebook_path: Path,
    *,
    output_dir: Path,
    output_basename: str,
    hide_input: bool,
) -> None:
    command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "pdf",
        "--PDFExporter.latex_command=['xelatex','{filename}']",
        "--output-dir",
        str(output_dir),
        "--output",
        output_basename,
    ]
    if hide_input:
        command.append("--no-input")
    command.append(str(notebook_path))

    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        raise RuntimeError(
            "Notebook PDF export failed. Confirm nbconvert and xelatex are installed."
        )


def export_notebook_pdf(
    notebook: str | Path,
    *,
    author: str = "Brittany L. Bales",
    date: str | None = None,
    output_dir: str | Path | None = None,
    hide_input: bool = True,
) -> Path:
    """Sanitize and export a notebook, returning the expected PDF path."""

    notebook_path = Path(notebook).expanduser().resolve()
    if not notebook_path.is_file():
        raise FileNotFoundError(f"Notebook not found: {notebook_path}")
    if notebook_path.suffix.lower() != ".ipynb":
        raise ValueError("notebook must have an .ipynb extension")

    destination = (
        Path(output_dir).expanduser().resolve()
        if output_dir is not None
        else notebook_path.parent
    )
    destination.mkdir(parents=True, exist_ok=True)

    loaded = nbformat.read(notebook_path, as_version=4)
    cleaned = sanitize_notebook(loaded)

    base_name = notebook_path.stem
    cleaned.metadata["title"] = title_from_filename(base_name)
    cleaned.metadata["date"] = date or format_today()
    cleaned.metadata["name"] = base_name
    if author:
        cleaned.metadata["authors"] = [{"name": author}]

    with tempfile.TemporaryDirectory() as temporary_directory:
        clean_path = Path(temporary_directory) / notebook_path.name
        nbformat.write(cleaned, clean_path)
        _run_nbconvert(
            clean_path,
            output_dir=destination,
            output_basename=base_name,
            hide_input=hide_input,
        )

    return destination / f"{base_name}.pdf"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sanitize a Jupyter notebook and export it to PDF."
    )
    parser.add_argument("notebook", help="Path to a .ipynb notebook")
    parser.add_argument("--author", default="Brittany L. Bales", help="Author metadata")
    parser.add_argument("--date", default=None, help="Date metadata")
    parser.add_argument("--output-dir", default=None, help="PDF output directory")
    parser.add_argument(
        "--show-input",
        action="store_true",
        help="Include code-cell input in the exported PDF",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        output = export_notebook_pdf(
            args.notebook,
            author=args.author,
            date=args.date,
            output_dir=args.output_dir,
            hide_input=not args.show_input,
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    print(f"Created: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
