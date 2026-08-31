from __future__ import annotations

import json
import mimetypes
import os
from pathlib import Path

import requests

from .models import TranscriptionResult


MATHPIX_ENDPOINT = "https://api.mathpix.com/v3/text"
SUPPORTED_IMAGE_SUFFIXES = {
    ".bmp",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}


class MathpixCredentialsError(RuntimeError):
    """Raised when Mathpix API credentials are not configured."""


class MathpixTranscriber:
    """Transcribe handwritten math with the Mathpix image OCR API."""

    def __init__(
        self,
        *,
        app_id: str | None = None,
        app_key: str | None = None,
        endpoint: str = MATHPIX_ENDPOINT,
        timeout_seconds: float = 30.0,
    ) -> None:
        self.app_id = app_id or os.getenv("MATHPIX_APP_ID", "")
        self.app_key = app_key or os.getenv("MATHPIX_APP_KEY", "")
        self.endpoint = endpoint
        self.timeout_seconds = timeout_seconds

    def transcribe(self, image_path: str | Path) -> TranscriptionResult:
        path = Path(image_path).expanduser().resolve()
        self._validate_image(path)
        self._validate_credentials()

        content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        options = {
            "formats": ["text"],
            "include_line_data": True,
        }

        with path.open("rb") as image_file:
            try:
                response = requests.post(
                    self.endpoint,
                    headers={
                        "app_id": self.app_id,
                        "app_key": self.app_key,
                    },
                    files={
                        "file": (path.name, image_file, content_type),
                    },
                    data={
                        "options_json": json.dumps(options),
                    },
                    timeout=self.timeout_seconds,
                )
            except requests.RequestException as exc:
                raise RuntimeError(f"Mathpix request failed: {exc}") from exc

        if not response.ok:
            detail = response.text.strip()
            raise RuntimeError(
                f"Mathpix OCR failed with HTTP {response.status_code}"
                + (f": {detail}" if detail else ".")
            )

        try:
            payload = response.json()
        except ValueError as exc:
            raise RuntimeError("Mathpix OCR returned output that was not valid JSON.") from exc

        latex = str(payload.get("latex_styled", "")).strip()
        if not latex:
            raise RuntimeError(
                "Mathpix OCR did not return latex_styled for this image."
            )

        raw_confidence = payload.get("confidence")
        confidence = (
            float(raw_confidence)
            if raw_confidence is not None
            else None
        )

        return TranscriptionResult(
            source=path,
            latex=latex,
            confidence=confidence,
            provider="mathpix",
        )

    def _validate_credentials(self) -> None:
        missing = []
        if not self.app_id:
            missing.append("MATHPIX_APP_ID")
        if not self.app_key:
            missing.append("MATHPIX_APP_KEY")

        if missing:
            raise MathpixCredentialsError(
                "Missing Mathpix credentials: "
                + ", ".join(missing)
                + ". Set them as environment variables before running math-transcribe."
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
