from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TranscriptionResult:
    """A literal OCR transcription of one handwritten math image."""

    source: Path
    latex: str
    confidence: float | None
    provider: str

    def as_markdown_math(self) -> str:
        """Wrap the recognized LaTeX in a notebook-friendly display block."""
        return f"$$\n{self.latex}\n$$"
