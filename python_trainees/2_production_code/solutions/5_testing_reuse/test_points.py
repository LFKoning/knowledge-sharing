"""Unit tests for the Point2D class."""
import pytest
from points import Points2D


@pytest.fixture
def points():
    """Return a sample Poins2D object."""
    return Points2D((1, 1), (1, 3), (4, 1), (4, 3))


@pytest.mark.parametrize(
    argnames=["delta_x", "delta_y", "expected"],
    argvalues=[
        ( 2,  3, [( 3,  4), ( 3, 6), (6,  4), (6, 6)]),
        (-2, -3, [(-1, -2), (-1, 0), (2, -2), (2, 0)]),
    ],
    ids=["Move positive", "Move negative"]
)
def test_move(points, delta_x, delta_y, expected):
    """Test moving 2D points."""
    points.move(delta_x, delta_y)
    assert points._points == expected


@pytest.mark.parametrize(
    argnames=["scale_x", "scale_y", "expected"],
    argvalues=[
        ( 2,  3, [( 2,  3), ( 2,  9), ( 8,  3), ( 8,  9)]),
        (-2, -3, [(-2, -3), (-2, -9), (-8, -3), (-8, -9)]),
    ],
    ids=["Scale positive", "Scale negative"]
)
def test_scale(points, scale_x, scale_y, expected):
    """Test scaling 2D points."""
    points.scale(scale_x, scale_y)
    assert points._points == expected
