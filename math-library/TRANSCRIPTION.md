# Handwritten Math Transcription

The transcription command converts an image of handwritten mathematics into literal LaTeX.

Its scope is intentionally narrow for coursework use:

- transcribe what is written,
- report OCR confidence when available,
- optionally wrap the result in a notebook-friendly display-math block.

It does **not** simplify expressions, solve problems, correct mathematical errors, fill in missing steps, or suggest the next step.

## Install the Local OCR Engine

`math-transcribe` uses the external MathCraft OCR command in formula mode. Install its CPU runtime in the same virtual environment:

```powershell
python -m pip install "mathcraft-ocr[cpu]"
```

Check the local runtime:

```powershell
mathcraft doctor --provider auto
```

The model files are downloaded locally by MathCraft when needed.

## Transcribe an Image

Return only the recognized LaTeX:

```powershell
math-transcribe .\handwritten\assignments\work.jpg
```

Return a notebook-ready display block:

```powershell
math-transcribe .\handwritten\assignments\work.jpg --format markdown
```

Return OCR metadata, including confidence:

```powershell
math-transcribe .\handwritten\assignments\work.jpg --format json
```

Example JSON shape:

```json
{
  "source": "C:\\path\\to\\work.jpg",
  "latex": "\\int \\sin^2(x)\\cos^2(x)\\,dx",
  "confidence": 0.93,
  "provider": "CPUExecutionProvider"
}
```

## Design Boundary

The `coursework_math.transcription` package deliberately treats OCR output as data. The recognized LaTeX is passed through without algebraic or calculus transformations.

Any future notebook-editor integration should preserve that boundary: importing or inserting the transcription is allowed, but mathematical evaluation and correction should remain outside this workflow.
