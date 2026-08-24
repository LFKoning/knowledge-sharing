"""Unit tests for the utils module."""
import pytest
from utils import mean, absmean


# Tests for mean


def test_mean_postive():
    """Test mean with positive numbers."""
    assert mean([1, 2, 3]) == 2


def test_mean_negative():
    """Test mean with negative numbers."""
    assert mean([-4, -5, -6]) == -5


def test_mean_missing_included():
    """Test mean with missing values included."""
    assert mean([1, 2, 3, None], dropna=False) == 6 / 4


def test_mean_missing_excluded():
    """Test mean with missing values included."""
    assert mean([1, 2, 3, None], dropna=True) == 6 / 3


def test_mean_error_empty():
    """Test mean ValueError on empty list."""
    with pytest.raises(ValueError) as error:
        mean([])
    assert error.match("List of values is empty.")


def test_mean_error_nonnumeric():
    """Test mean TypeError on nonnumeric values."""
    with pytest.raises(TypeError) as error:
        mean(["a", "b", "c"])
    assert error.match("List contains non-numeric values.")


def test_mean_error_no_list():
    """Test mean TypeError on non-list."""
    with pytest.raises(TypeError) as error:
        mean(None)
    assert error.match("List contains non-numeric values.")


# Tests for absmean


def test_absmean_postive():
    """Test absmean with positive numbers."""
    assert absmean([1, 2, 3]) == 2


def test_absmean_negative():
    """Test absmean with negative numbers."""
    assert absmean([-4, -5, -6]) == 5


def test_absmean_mixed():
    """Test absmean with positive and negative numbers."""
    assert absmean([4, -5, 6]) == 5


def test_absmean_woops():
    """Test absmean with positive and negative numbers."""
    with pytest.raises(TypeError) as error:
        absmean([4, "A", 6])
    assert error.match("List contains non-numeric values.")
