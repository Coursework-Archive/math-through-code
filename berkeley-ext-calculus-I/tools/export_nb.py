#!/usr/bin/env python3
"""
Sanitize a .ipynb (remove non-nbformat keys like 'jetTransient')
and export to HTML with no input, preserving the original base filename.

Usage:
  python export_nb.py path/to/notebook.ipynb
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from copy import deepcopy

import nbformat


BAD_KEYS_IN_OUTPUTS = {
    "jetTransient",
}

BAD_KEYS_IN_CELL = set()


def sanitize_notebook(nb: nbformat.NotebookNode) -> nbformat.NotebookNode:
    nb2 = deepcopy(nb)

    for cell in nb2.get("cells", []):
        for k in list(cell.keys()):
            if k in BAD_KEYS_IN_CELL:
                cell.pop(k, None)

        outputs = cell.get("outputs")
        if isinstance(outputs, list):
            for out in outputs:
                if isinstance(out, dict):
                    for k in list(out.keys()):
                        if k in BAD_KEYS_IN_OUTPUTS:
                            out.pop(k, None)

                    md = out.get("metadata")
                    if isinstance(md, dict):
                        md.pop("jetTransient", None)

    return nb2


def run_nbconvert(clean_ipynb: str, output_dir: str, output_basename: str) -> None:
    """
    output_basename should be the filename WITHOUT extension.
    nbconvert will write output_basename.html into output_dir.
    """
    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "html",
        "--no-input",
        "--output-dir",
        output_dir,
        "--output",
        output_basename,
        clean_ipynb,
    ]
    subprocess.run(cmd, check=True)


def fix_html_title(html_path: str, title: str) -> None:
    with open(html_path, "r", encoding="utf-8") as f:
        s = f.read()

    s = re.sub(
        r"<title>.*?</title>",
        f"<title>{title}</title>",
        s,
        count=1,
        flags=re.DOTALL,
    )

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(s)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook", help="Path to .ipynb")
    args = parser.parse_args()

    ipynb_path = os.path.abspath(args.notebook)
    if not os.path.exists(ipynb_path):
        print(f"File not found: {ipynb_path}", file=sys.stderr)
        return 2

    nb = nbformat.read(ipynb_path, as_version=4)
    nb_clean = sanitize_notebook(nb)

    output_dir = os.path.dirname(ipynb_path)
    base_name = os.path.splitext(os.path.basename(ipynb_path))[0]

    # Helps nbconvert pick a sensible title in some setups
    nb_clean.metadata["name"] = base_name

    with tempfile.NamedTemporaryFile(mode="w", suffix=".ipynb", delete=False, encoding="utf-8") as tmp:
        nbformat.write(nb_clean, tmp.name)
        temp_ipynb = tmp.name

    try:
        run_nbconvert(temp_ipynb, output_dir, base_name)

        html_path = os.path.join(output_dir, base_name + ".html")
        fix_html_title(html_path, base_name)
    finally:
        os.remove(temp_ipynb)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
