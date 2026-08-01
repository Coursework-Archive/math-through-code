"""Compatibility command for the installable notebook exporter."""

from __future__ import annotations

import sys
from pathlib import Path

_SOURCE = Path(__file__).resolve().parents[1] / "src"
if str(_SOURCE) not in sys.path:
    sys.path.insert(0, str(_SOURCE))

from coursework_math.notebooks.export import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
