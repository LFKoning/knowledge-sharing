"""Module for a dict that is case-insensitive."""

from collections import UserDict


class FuzzyDict(UserDict):
    """Dict-class that is case insensitive."""

    def __getitem__(self, key):
        """Get a key from the data."""
        key = key.lower().strip()
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        """Set a key in the data."""
        key = key.lower().strip()
        super().__setitem__(key, value)
