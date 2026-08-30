from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Sequence

from .models import TranscriptionResult


SUPPORTED_IMAGE_SUFFIXES = {
    ".bmp",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}


class MathCraftUnavailableError(RuntimeError):
    """Raised when the external MathCraft OCR command is not installed."""


class MathCraftTranscriber:
    """Transcribe handwritten math using MathCraft's local formula OCR mode."""

    def __init__(
        self,
        *,
        provider: str = "auto",
        command: Sequence[str] = ("mathcraft",),
    ) -> None:
        self.provider = provider
        self.command = tuple(command)

    def transcribe(self, image_path: str | Path) -> TranscriptionResult:
        path = Path(image_path).expanduser().resolve()
        self._validate_image(path)

        args = [
            *self.command,
            "ocr",
            str(path),
            "--profile",
            "formula",
            "--provider",
            self.provider,
            "--json",
        ]

        try:
            completed = subprocess.run(
                args,
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
        except FileNotFoundError as exc:
            raise MathCraftUnavailableError(
                "MathCraft OCR is not installed. Install it separately with "
                "'pip install \"mathcraft-ocr[cpu]\"' and retry."
            ) from exc

        if completed.returncode != 0:
            detail = completed.stderr.strip() or completed.stdout.strip()
            raise RuntimeError(
                "MathCraft OCR failed"
                + (f": {detail}" if detail else ".")
            )

        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "MathCraft OCR returned output that was not valid JSON."
            ) from exc

        latex = str(payload.get("text", "")).strip()
        if not latex:
            raise RuntimeError("MathCraft OCR did not recognize any math.")

        raw_score = payload.get("score")
        confidence = float(raw_score) if raw_score is not None else None
        provider = str(payload.get("provider") or self.provider)

        return TranscriptionResult(
            source=path,
            latex=latex,
            confidence=confidence,
            provider=provider,
        )

    @staticmethod
    def _validate_image(path: Path) -> None:
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {path}")
        if not path.is_file():
            raise ValueError(f"Expected an image file: {path}")
        if path.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
            raise ValueError(
                f"Unsupported image type '{path.suffix}'. "
                f"Supported types: {', '.join(sorted(SUPPORTED_IMAGE_SUFFIXES))}"
            )
