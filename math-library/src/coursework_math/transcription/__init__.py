"""Literal handwritten-math transcription utilities.

This package intentionally performs transcription only. It does not simplify,
solve, correct, or complete mathematical work.
"""

from .mathcraft import MathCraftTranscriber, MathCraftUnavailableError
from .mathpix import MathpixCredentialsError, MathpixTranscriber
from .models import TranscriptionResult

__all__ = [
    "MathCraftTranscriber",
    "MathCraftUnavailableError",
    "MathpixCredentialsError",
    "MathpixTranscriber",
    "TranscriptionResult",
]
