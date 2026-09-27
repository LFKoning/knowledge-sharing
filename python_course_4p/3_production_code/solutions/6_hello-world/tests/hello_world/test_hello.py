"""Unit tests for the hello module."""
from hello_world.hello import say_hi


def test_say_hi():
    """Test say_hi functionality"""
    assert say_hi() == "Hello World!"
