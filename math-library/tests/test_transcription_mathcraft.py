from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from coursework_math.transcription import (
    MathCraftTranscriber,
    MathCraftUnavailableError,
)


def test_transcribe_returns_literal_mathcraft_output(tmp_path: Path) -> None:
    image = tmp_path / "work.png"
    image.write_bytes(b"fake-image")

    response = {
        "text": r"\int \sin^2(x)\cos^2(x)\,dx",
        "score": 0.93,
        "provider": "CPUExecutionProvider",
    }

    completed = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout=json.dumps(response),
        stderr="",
    )

    with patch("coursework_math.transcription.mathcraft.subprocess.run", return_value=completed):
        result = MathCraftTranscriber().transcribe(image)

    assert result.latex == response["text"]
    assert result.confidence == 0.93
    assert result.provider == "CPUExecutionProvider"
    assert result.as_markdown_math() == f"$$\n{response['text']}\n$$"


def test_transcribe_does_not_modify_recognized_latex(tmp_path: Path) -> None:
    image = tmp_path / "work.jpg"
    image.write_bytes(b"fake-image")
    literal_output = r"u=cos(x)"

    completed = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout=json.dumps(
            {
                "text": literal_output,
                "score": 0.71,
                "provider": "CPUExecutionProvider",
            }
        ),
        stderr="",
    )

    with patch("coursework_math.transcription.mathcraft.subprocess.run", return_value=completed):
        result = MathCraftTranscriber().transcribe(image)

    assert result.latex == literal_output


def test_missing_image_is_rejected(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        MathCraftTranscriber().transcribe(tmp_path / "missing.png")


def test_missing_mathcraft_command_has_clear_error(tmp_path: Path) -> None:
    image = tmp_path / "work.png"
    image.write_bytes(b"fake-image")

    with patch(
        "coursework_math.transcription.mathcraft.subprocess.run",
        side_effect=FileNotFoundError,
    ):
        with pytest.raises(MathCraftUnavailableError, match="MathCraft OCR is not installed"):
            MathCraftTranscriber().transcribe(image)
