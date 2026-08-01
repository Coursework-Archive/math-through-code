from PIL import Image as PILImage, ImageOps
from IPython.display import display, Image
import tempfile
from pathlib import Path


def show_image(path: str | Path, width: int | None = None) -> None:
    """
    Display an image in a Jupyter notebook with automatic EXIF rotation correction.

    Parameters
    ----------
    path : str or Path
        Path to the image file.
    width : int, optional
        Display width in pixels.
    """
    path = Path(path)

    img = PILImage.open(path)
    img = ImageOps.exif_transpose(img)  # Fixes rotated images

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        img.save(tmp.name)
        display(Image(filename=tmp.name, width=width))