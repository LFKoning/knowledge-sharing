"""Unit tests for FuzzyDict class."""

from fuzzy_dict import FuzzyDict

# Create a FuzzyDict for testing.
fdict = FuzzyDict()
fdict["test"] = "test value"


def test_update_key():
    """Test FuzzyDict update key."""
    fdict["TEST"] = "new value"
    assert fdict.data["test"] == "new value"


def test_get_key():
    """Test FuzzyDict get key."""
    assert fdict["TEST"] == "test value"
