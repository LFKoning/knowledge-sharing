"""Module containing unit tests for helper functions."""
from utils import mean


def test_mean_positive():
    """Test mean function."""
    numbers = [1, 2, 3, 4]
    expected = 10 / 4

    # Use assert to define the unit test.
    assert mean(numbers) == expected
