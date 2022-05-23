"""Module containing unit tests for helper functions."""
import pytest

from helpers import mean


@pytest.mark.parametrize(
    argnames=["numbers", "expected"],
    argvalues=[
        ([1, 2, 3], 2),
    ],
     ids=[
        "Positive numbers",
     ]
)
def test_mean_parameters(numbers, expected):
    """Test mean function using parameters"""
    assert mean(numbers) == expected
