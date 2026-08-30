from __future__ import annotations

import argparse
import json
from pathlib import Path

from .mathcraft import MathCraftTranscriber


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="math-transcribe",
        description=(
            "Convert a handwritten math image to literal LaTeX. "
            "This command does not solve or correct the mathematics."
        ),
    )
    parser.add_argument("image", help="Path to a handwritten math image")
    parser.add_argument(
        "--provider",
        default="auto",
        help="MathCraft execution provider (default: auto)",
    )
    parser.add_argument(
        "--format",
        choices=("latex", "markdown", "json"),
        default="latex",
        dest="output_format",
        help="Output format (default: latex)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    result = MathCraftTranscriber(provider=args.provider).transcribe(
        Path(args.image)
    )

    if args.output_format == "markdown":
        print(result.as_markdown_math())
    elif args.output_format == "json":
        print(
            json.dumps(
                {
                    "source": str(result.source),
                    "latex": result.latex,
                    "confidence": result.confidence,
                    "provider": result.provider,
                },
                indent=2,
            )
        )
    else:
        print(result.latex)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
