from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest

from coursework_math.plotting import plot_data_points


def test_point_labels_disabled_by_default() -> None:
    ax = plot_data_points([1, 2], [0.5, 0.75], connect=False, show=False)
    try:
        assert ax.texts == []
    finally:
        plt.close(ax.figure)


def test_point_labels_show_four_decimal_places() -> None:
    ax = plot_data_points(
        [1, 2],
        [0.5, 0.75],
        connect=False,
        annotate_points=True,
        show=False,
    )
    try:
        assert [text.get_text() for text in ax.texts] == ["0.5000", "0.7500"]
    finally:
        plt.close(ax.figure)


def test_point_label_precision_can_be_customized() -> None:
    ax = plot_data_points(
        [1], [0.125], connect=False, annotate_points=True,
        annotation_precision=2, show=False,
    )
    try:
        assert [text.get_text() for text in ax.texts] == ["0.12"]
    finally:
        plt.close(ax.figure)


def test_negative_annotation_precision_is_rejected() -> None:
    with pytest.raises(ValueError, match="annotation_precision must be nonnegative"):
        plot_data_points([1], [0.5], annotation_precision=-1, show=False)
