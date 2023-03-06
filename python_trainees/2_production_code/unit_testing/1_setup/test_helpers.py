"""Module containing unit tests for helper functions."""
from helpers import mean


def test_mean():
    """Test mean function."""
    numbers = [1, 2, 3, 4]
    expected = 10 / 4

    # Assert turns it into a test
    assert mean(numbers) == expected
