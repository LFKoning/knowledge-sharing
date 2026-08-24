"""Module for the ValueCounter class."""


class ValueCounter:
    """Keeps counts of value frequencies."""

    def __init__(self):
        self._counts = {}

    def update(self, values: list):
        """Update value frequencies.

        Parameters
        ----------
        values : list
            List of values to track frequenceis for.
        """
        for value in values:
            if value in self._counts:
                self._counts[value] += 1
            else:
                self._counts[value] = 1

    def top(self, n=1):
        """Return the most frequent values.

        Parameters
        ----------
        n : int
            Number of values to return.

        Returns
        -------
        list of tuples
            List of tuples of value and correspondg frequency.
        """
        result = []
        sorted_keys = sorted(self._counts, key=lambda k: self._counts[k], reverse=True)
        for key in sorted_keys[:n]:
            result.append((key, self._counts[key]))
        return result

    def bottom(self, n=1):
        """Return the least frequent values.

        Parameters
        ----------
        n : int
            Number of values to return.

        list of tuples
            List of tuples of value and correspondg frequency.
        """
        result = []
        sorted_keys = sorted(self._counts, key=lambda k: self._counts[k])
        for key in sorted_keys[:n]:
            result.append((key, self._counts[key]))
        return result

    def reset(self, key=None):
        """Reset frequency counters.

        Parameters
        ----------
        key : any, optional
            Key to reset frequency counts for.
            If omitted, reset all frequency counts.
        """
        if key is not None:
            if key not in self._counts:
                raise KeyError(f"Key {key} not found in frequency counts.")
            self._counts[key] = 0

        else:
            self._counts = {}
