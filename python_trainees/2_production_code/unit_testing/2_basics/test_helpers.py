"""Module containing unit tests for helper functions."""
import pytest

from helpers import mean


def test_mean_positive_numbers():
    """Test mean for a list of positive numbers."""
    numbers = [1, 2, 3, 4]
    expected = 2.5
    assert mean(numbers) == expected


def test_mean_negative_numbers():
    """Test mean for a list of negative numbers."""
    numbers = [-10, -20, -30]
    expected = -20.0
    assert mean(numbers) == expected


def test_mean_missing_values():
    """Test mean for list with missing values."""
    numbers = [1, 2, 3, 4, None, None]
    expected = 10 / 6
    assert mean(numbers) == expected


def test_mean_drop_missing_values():
    """Test mean for valid list of numbers."""
    numbers = [1, 2, 3, 4, None, None]
    expected = 10 / 4
    assert mean(numbers, dropna=True) == expected


def test_mean_error_no_list():
    """Test error when input is not list or tuple."""
    with pytest.raises(TypeError):
        mean(1)


def test_mean_error_non_numeric():
    """Test error when input is non-numeric."""
    with pytest.raises(ValueError) as error:
        mean(["A"])
    assert error.match("Cannot compute mean for non-numeric input.")


@pytest.mark.xfail(raises=ValueError)
def test_mean_error_non_numeric_xfail():
    """Test error when input is non-numeric using xfail."""
    mean(["A"])
