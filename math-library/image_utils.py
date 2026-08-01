"""Compatibility wrapper for older notebooks.

New code should import from ``coursework_math.images`` after installing the package.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent / "src"
if str(_SOURCE) not in sys.path:
    sys.path.insert(0, str(_SOURCE))

from coursework_math.images import load_image, show_image  # noqa: E402

__all__ = ["load_image", "show_image"]
