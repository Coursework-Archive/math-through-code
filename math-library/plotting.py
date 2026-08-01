"""Compatibility wrapper for older notebooks.

New code should import from ``coursework_math.plotting`` after installing the package.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SOURCE = Path(__file__).resolve().parent / "src"
if str(_SOURCE) not in sys.path:
    sys.path.insert(0, str(_SOURCE))

from coursework_math.plotting import *  # noqa: F403,E402
from coursework_math.plotting import __all__  # noqa: E402,F401
