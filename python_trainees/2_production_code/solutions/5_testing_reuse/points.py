"""Module for 2D point transformations."""


class Points2D:
    """Class for 2D point transformations.

    Parameters
    ----------
    *points : tuples
        Points provided as (x, y) tuples for each 2D point.
    """

    def __init__(self, *points):
        self._points = points

    def move(self, delta_x, delta_y):
        """Move points by x and y units."""
        self._points = [
            (x + delta_x, y + delta_y)
            for (x, y) in self._points
        ]

    def scale(self, scale_x, scale_y):
        """Scale points by x and y units."""
        self._points = [
            (x * scale_x, y * scale_y)
            for (x, y) in self._points
        ]
