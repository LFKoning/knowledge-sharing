"""Unit tests for FuzzyDict class."""

import pytest
from fuzzy_dict import FuzzyDict


@pytest.fixture
def fuzzy_dict():
    """Create a FuzzyDict for testing."""
    fd = FuzzyDict()
    fd["test"] = "test value"
    return fd


def test_update_key(fuzzy_dict):
    """Test FuzzyDict update key."""
    fuzzy_dict["TEST"] = "new value"
    assert fuzzy_dict.data["test"] == "new value"


def test_get_key(fuzzy_dict):
    """Test FuzzyDict get key."""
    assert fuzzy_dict["TEST"] == "test value"
