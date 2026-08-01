"""Image loading and display utilities for notebook coursework."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path


def load_image(path: str | Path):
    """Load an image, correct EXIF orientation, and return an independent copy."""

    try:
        from PIL import Image, ImageOps
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "Image utilities require Pillow. Install coursework-math[notebook]."
        ) from exc

    image_path = Path(path).expanduser().resolve()
    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    with Image.open(image_path) as image:
        return ImageOps.exif_transpose(image).copy()


def show_image(path: str | Path, width: int | None = None) -> None:
    """Display an EXIF-corrected image in Jupyter without temporary files."""

    if width is not None and width <= 0:
        raise ValueError("width must be a positive integer")

    try:
        from IPython.display import Image as NotebookImage
        from IPython.display import display
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "show_image() requires IPython. Install coursework-math[notebook]."
        ) from exc

    image = load_image(path)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    display(NotebookImage(data=buffer.getvalue(), width=width))
