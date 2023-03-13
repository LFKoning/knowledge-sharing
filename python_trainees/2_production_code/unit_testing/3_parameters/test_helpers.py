"""Module containing unit tests for helper functions."""
import pytest

from helpers import mean


@pytest.mark.parametrize(

    # Test function arguments to parametrize.
    argnames=["numbers", "expected"],

    # Argument values as tuples.
    argvalues=[
        ([ 1,    2,    3],  2),
        ([-1,   -2,   -3], -2),
        ([ 1,    2, None],  1),
    ],

    # Descriptive names for test scenarios.
    ids=[
        "Positive numbers",
        "Negative numbers",
        "Missing value",
    ]
)
def test_mean_parameters(numbers, expected):
    """Test mean function using parameters."""
    assert mean(numbers) == expected
