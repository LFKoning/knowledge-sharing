"""Module for unit tests using pandas data structures."""
from codecs import ignore_errors
import pandas as pd


def test_series():
    """Test whether two Series are identical."""
    expected = pd.Series([1., 2., 3., 4.])
    cleansed = pd.Series([1, 2, 3, 4, None]).dropna()
    pd.testing.assert_series_equal(cleansed, expected)


def test_series_ignore_dtype():
    """Test whether two Series are equal, ignoring data types."""
    expected = pd.Series([1, 2, 3, 4])
    cleansed = pd.Series([1, 2, 3, 4, None]).dropna()
    pd.testing.assert_series_equal(cleansed, expected, check_dtype=False)


def test_series_tolerance():
    """Test whether two Series are approximately equal."""
    float_series = pd.Series([1.001, 2.002, 3.003])
    expected = pd.Series([1., 2., 3.])
    pd.testing.assert_series_equal(float_series, expected, atol=.005)


def test_dataframe():
    """Test whether DataFrames are equal."""
    df = pd.DataFrame({
        "x": [4, 2, 3, 1],
        "y": [1, 0, 1, 0],
    })
    expected = df.astype(float)
    pd.testing.assert_frame_equal(df, expected, check_dtype=False)


def test_dataframe_ignore_order():
    """Test whether DataFrames match ignoring row and column order."""
    df = pd.DataFrame({
        "x": [4, 2, 3, 1],
        "y": [1, 0, 1, 0],
    })
    expected = df.sort_values("x")[["y", "x"]]
    pd.testing.assert_frame_equal(df, expected, check_like=True)
