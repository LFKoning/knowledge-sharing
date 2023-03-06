"""Module containing unit tests for configuration helper functions."""
import pytest

from dict_tools import recursive_update


# Create a fixture for use in tests.
# Note: Fixture runs every time it appears in a test!
@pytest.fixture
def defaults():
    """Generate a default dictionairy."""
    return {
        "integer_value": 1,
        "dict_value": {
            "A": 1,
            "B": 2,
        },
    }


# Note: The fixture is provided as a test argument.
def test_add_new_key(defaults):
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


def test_overwrite_simple_key(defaults):
    """Test overwriting a simple key."""
    overwrite = {"integer_value": 100}
    expected = {
        "integer_value": 100,
        "dict_value": {
            "A": 1,
            "B": 2,
        }
    }

    assert recursive_update(overwrite, defaults) == expected
