# tools/export_np.py
"""
Sanitize a .ipynb (remove non-nbformat keys like 'jetTransient')
and export to PDF with no input, preserving the original base filename.

Usage:
  python tools/export_nb.py path/to/notebook.ipynb
  python tools/export_nb.py path/to/notebook.ipynb --author "Your Name"
  python tools/export_nb.py path/to/notebook.ipynb --date "February 8, 2026"
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
from copy import deepcopy
from datetime import datetime
from nbformat.v4 import new_markdown_cell
import nbformat

BAD_KEYS_IN_OUTPUTS = {"jetTransient"}
BAD_KEYS_IN_CELL: set[str] = set()


def format_today():
    return datetime.now().strftime("%B %d, %Y").replace(" 0", " ")


def sanitize_notebook(nb: nbformat.NotebookNode) -> nbformat.NotebookNode:
    nb2 = deepcopy(nb)

    for cell in nb2.get("cells", []):
        # Remove any unwanted top-level cell keys (currently none)
        for k in list(cell.keys()):
            if k in BAD_KEYS_IN_CELL:
                cell.pop(k, None)

        outputs = cell.get("outputs")
        if isinstance(outputs, list):
            for out in outputs:
                if isinstance(out, dict):
                    # Remove bad keys directly on output dict
                    for k in list(out.keys()):
                        if k in BAD_KEYS_IN_OUTPUTS:
                            out.pop(k, None)

                    # Remove bad keys in output metadata dict
                    md = out.get("metadata")
                    if isinstance(md, dict):
                        md.pop("jetTransient", None)

    return nb2


def append_disclaimer(nb):
    disclaimer = r"""
\vfill

---

\begin{center}
\small
ChatGPT was used for Markdown and \LaTeX\ formatting assistance.  
All mathematical reasoning, derivations, and conclusions are my own work and were independently checked for correctness.
\end{center}
"""
    nb.cells.append(new_markdown_cell(disclaimer))

def title_from_filename(base_name: str) -> str:
    """
    Convert 'module_2_assignments' -> 'Module 2 Assignments'
    """
    words = base_name.replace("_", " ").split()
    return " ".join(w if w.isdigit() else w.capitalize() for w in words)


def run_nbconvert_pdf(clean_ipynb: str, output_dir: str, output_basename: str) -> None:
    """
    nbconvert writes output_basename.pdf into output_dir.
    """
    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "pdf",
        "--no-input",
        "--output-dir",
        output_dir,
        "--output",
        output_basename,
        clean_ipynb,
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", help="Path to .ipynb")
    parser.add_argument(
        "--author",
        default="Brittany L. Bales",
        help="Author name to store in notebook metadata (default: Brittany L. Bales)",
    )
    parser.add_argument(
        "--date",
        default=None,
        help="Date string to store in notebook metadata (default: today's date). Example: 'February 8, 2026'",
    )
    args = parser.parse_args()

    ipynb_path = os.path.abspath(args.notebook)
    if not os.path.exists(ipynb_path):
        print(f"File not found: {ipynb_path}", file=sys.stderr)
        return 2

    nb = nbformat.read(ipynb_path, as_version=4)
    nb_clean = sanitize_notebook(nb)

    # append_disclaimer(nb_clean)

    output_dir = os.path.dirname(ipynb_path)
    base_name = os.path.splitext(os.path.basename(ipynb_path))[0]

    # Derived title + date
    title = title_from_filename(base_name)
    datestr = args.date if args.date else format_today()
    author = args.author

    # Metadata (harmless even if your template doesn't use it)
    nb_clean.metadata["title"] = title
    nb_clean.metadata["authors"] = [{"name": author}]
    nb_clean.metadata["date"] = datestr
    nb_clean.metadata["name"] = base_name  # important: helps avoid tmpxxxxx naming

    # Write sanitized notebook to a temp folder but keep the *real* base filename
    with tempfile.TemporaryDirectory() as td:
        temp_ipynb = os.path.join(td, base_name + ".ipynb")
        nbformat.write(nb_clean, temp_ipynb)

        run_nbconvert_pdf(temp_ipynb, output_dir, base_name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
