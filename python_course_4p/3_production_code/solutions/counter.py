"""Module for the ValueCounter class."""


class ValueCounter:
    """Class for keeping track of value frequencies.

    Examples
    --------
    >>> counter = ValueCounter()
    >>> counter.update(["a", "a", "a", "b", "b", "c"])
    >>> print(counter.top())
    {"a": 3}
    >>> print(counter.bottom(2))
    {"c": 1, "b": 2}
    """

    def __init__(self):
        self._counts = {}

    def update(self, values: list):
        """Update value frequencies.

        Parameters
        ----------
        values : list
            List of values to track frequencies for.
        """
        for value in values:
            if value in self._counts:
                self._counts[value] += 1
            else:
                self._counts[value] = 1

    def top(self, n=1):
        """Return the most frequent values as dict.

        Parameters
        ----------
        n : int
            Number of values to return.

        Returns
        -------
        list of tuples
            List of tuples of value and correspondg frequency.
        """
        # Reverse sort counts by frequency.
        sorted_keys = sorted(self._counts, key=lambda k: self._counts[k], reverse=True)
        return {key: self._counts[key] for key in sorted_keys[:n]}

    def bottom(self, n=1):
        """Return the least frequent values as dict.

        Parameters
        ----------
        n : int
            Number of values to return.

        list of tuples
            List of tuples of value and correspondg frequency.
        """
        # Sort counts by frequency.
        sorted_keys = sorted(self._counts, key=lambda k: self._counts[k])
        return {key: self._counts[key] for key in sorted_keys[:n]}
