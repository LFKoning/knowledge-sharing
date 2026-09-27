"""Unit tests for the ValueCounter class."""
import pytest
from counter import ValueCounter


@pytest.fixture
def counter():
    """Initialize ValueCounter with some values."""
    vc = ValueCounter()
    vc.update(["a", "a", "a", "b", "c", "c"])
    return vc

def test_update(counter):
    """Test updating counter frequencies."""
    counter.update(["a", "d"])
    assert counter._counts == {"a": 4, "b": 1, "c": 2, "d": 1}


def test_top(counter):
    """Test top without providing n."""
    assert counter.top() == [("a", 3)]


def test_top_3(counter):
    """Test top with n set to 3."""
    assert counter.top(3) == [("a", 3), ("c", 2), ("b", 1)]


def test_bottom(counter):
    """Test bottom without providing n."""
    assert counter.bottom() == [("b", 1)]


def test_bottom_3(counter):
    """Test bottom with n set to 3."""
    assert counter.bottom(3) == [("b", 1), ("c", 2), ("a", 3)]
