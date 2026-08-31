# Handwritten Math Transcription

The transcription command converts an image of handwritten mathematics into literal LaTeX.

Its scope is intentionally narrow for coursework use:

- transcribe what is written,
- report OCR confidence when available,
- optionally wrap the result in a notebook-friendly display-math block.

It does **not** simplify expressions, solve problems, correct mathematical errors, fill in missing steps, or suggest the next step.

## Primary OCR Engine: Mathpix

`math-transcribe` uses Mathpix by default because it supports OCR of handwritten equations from image uploads.

Create Mathpix API credentials, then set them in the current PowerShell session:

```powershell
$env:MATHPIX_APP_ID = "your-app-id"
$env:MATHPIX_APP_KEY = "your-app-key"
```

Do not commit API credentials to the repository.

Return only the recognized LaTeX:

```powershell
math-transcribe "$HOME\Downloads\work.jpg"
```

Return a notebook-ready display block:

```powershell
math-transcribe "$HOME\Downloads\work.jpg" --format markdown
```

Return OCR metadata, including confidence:

```powershell
math-transcribe "$HOME\Downloads\work.jpg" --format json
```

Example JSON shape:

```json
{
  "source": "C:\\path\\to\\work.jpg",
  "latex": "\\int \\sin^2(x)\\cos^2(x)\\,dx",
  "confidence": 0.97,
  "provider": "mathpix"
}
```

## Local Fallback: MathCraft

MathCraft remains available when a fully local workflow is preferred:

```powershell
math-transcribe "$HOME\Downloads\work.jpg" --engine mathcraft --format json
```

Install its CPU runtime separately if needed:

```powershell
python -m pip install "mathcraft-ocr[cpu]"
mathcraft warmup --profile formula --provider auto
```

## Design Boundary

The `coursework_math.transcription` package deliberately treats OCR output as data. The recognized LaTeX is passed through without algebraic or calculus transformations.

Mathpix output is not considered mathematically verified, even when the API reports high confidence. Review the rendered transcription before inserting it into coursework.

Any future notebook-editor integration should preserve that boundary: importing or inserting the transcription is allowed, but mathematical evaluation and correction should remain outside this workflow.
