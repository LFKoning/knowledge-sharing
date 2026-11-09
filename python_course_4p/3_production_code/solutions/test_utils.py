"""Unit tests for the utils module."""

import pytest
from utils import mean


def test_mean_postive():
    """Test mean with positive numbers."""
    assert mean([1, 2, 3]) == 2


def test_mean_negative():
    """Test mean with negative numbers."""
    assert mean([-4, -5, -6]) == -5


def test_mean_fill_missing():
    """Test mean with filling missing values."""
    assert mean([1, 2, 3, None], fillna=4) == 10 / 4


def test_mean_error_empty():
    """Test mean ValueError on empty list."""
    with pytest.raises(ValueError) as error:
        mean([])
    assert error.match("List of values is empty.")


def test_mean_error_nonnumeric():
    """Test mean TypeError on non-numeric values."""
    with pytest.raises(TypeError) as error:
        mean(["a", "b", "c"])
    assert error.match("List contains non-numeric values.")


def test_mean_error_no_list():
    """Test mean TypeError on non-list."""
    with pytest.raises(TypeError) as error:
        mean(None)
    assert error.match("List contains non-numeric values.")
