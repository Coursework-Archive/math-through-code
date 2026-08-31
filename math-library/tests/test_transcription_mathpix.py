from __future__ import annotations

from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from coursework_math.transcription import (
    MathpixCredentialsError,
    MathpixTranscriber,
)


def test_mathpix_returns_literal_latex(tmp_path: Path) -> None:
    image = tmp_path / "work.jpg"
    image.write_bytes(b"fake-image")

    response = Mock()
    response.ok = True
    response.json.return_value = {
        "latex_styled": r"\int_3^4 \frac{\tan^7(x)\sec^8(x)}{\sqrt{36+x^2}}\,dx",
        "confidence": 0.97,
    }

    with patch("coursework_math.transcription.mathpix.requests.post", return_value=response):
        result = MathpixTranscriber(
            app_id="test-app",
            app_key="test-key",
        ).transcribe(image)

    assert result.latex == response.json.return_value["latex_styled"]
    assert result.confidence == 0.97
    assert result.provider == "mathpix"


def test_mathpix_requires_credentials(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    image = tmp_path / "work.jpg"
    image.write_bytes(b"fake-image")
    monkeypatch.delenv("MATHPIX_APP_ID", raising=False)
    monkeypatch.delenv("MATHPIX_APP_KEY", raising=False)

    with pytest.raises(MathpixCredentialsError, match="MATHPIX_APP_ID"):
        MathpixTranscriber().transcribe(image)


def test_mathpix_uses_environment_credentials(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    image = tmp_path / "work.png"
    image.write_bytes(b"fake-image")
    monkeypatch.setenv("MATHPIX_APP_ID", "env-app")
    monkeypatch.setenv("MATHPIX_APP_KEY", "env-key")

    response = Mock()
    response.ok = True
    response.json.return_value = {
        "latex_styled": r"x^2+1",
        "confidence": 1.0,
    }

    with patch("coursework_math.transcription.mathpix.requests.post", return_value=response) as post:
        MathpixTranscriber().transcribe(image)

    assert post.call_args.kwargs["headers"]["app_id"] == "env-app"
    assert post.call_args.kwargs["headers"]["app_key"] == "env-key"


def test_mathpix_does_not_guess_when_latex_is_missing(tmp_path: Path) -> None:
    image = tmp_path / "work.jpg"
    image.write_bytes(b"fake-image")

    response = Mock()
    response.ok = True
    response.json.return_value = {
        "text": "some OCR text",
        "confidence": 0.8,
    }

    with patch("coursework_math.transcription.mathpix.requests.post", return_value=response):
        with pytest.raises(RuntimeError, match="did not return latex_styled"):
            MathpixTranscriber(
                app_id="test-app",
                app_key="test-key",
            ).transcribe(image)
