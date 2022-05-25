"""Module containing unit tests for configuration helper functions."""
import pytest

from dict_tools import recursive_update


# Turn into fixture!
defaults = {
    "integer_value": 1,
    "dict_value": {
        "A": 1,
        "B": 2,
    },
}


def test_add_new_key():
    """Test adding a new simple key - value pair."""
    new_value = {"string_value": "ABC"}
    expected = {
        "integer_value": 1,
        "dict_value": {
            "A": 1,
            "B": 2,
        },
        "string_value": "ABC",
    }
    assert recursive_update(new_value, defaults) == expected


def test_overwrite_simple_key():
    """Test overwriting a simple key."""
    overwrite = {"integer_value": 100}
    expected = {
        "integer_value": 100,
        "dict_value": {
            "A": 1,
            "B": 2,
        }
    }

    # Note: Fails due to previous test!
    assert recursive_update(overwrite, defaults) == expected
