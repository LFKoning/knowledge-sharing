"""Module for unit tests using pandas data structures."""
import pandas as pd


def cleanse_data(series):
    """Drops missing values."""
    return series.dropna()


def test_series():
    """Test whether two Series are identical."""
    data = pd.Series([1, 2, 3, None, 4, None])
    cleansed = cleanse_data(data)
    expected = pd.Series([1., 2., 3., 4.], index=[0, 1, 2, 4])

    # Test equality of two series.
    pd.testing.assert_series_equal(cleansed, expected)


def test_series_ignore_dtype():
    """Test whether two Series are equal, ignoring data types."""
    expected = pd.Series([1, 2, 3, 4])
    cleansed = pd.Series([1, 2, 3, 4, None]).dropna()

    # Check equality ignoring data types using check_dtype.
    pd.testing.assert_series_equal(cleansed, expected, check_dtype=False)


def test_series_tolerance():
    """Test whether two Series are approximately equal."""
    float_series = pd.Series([1.001, 2.002, 3.003])
    expected = pd.Series([1., 2., 3.])

    # Test equality with approximate values using atol.
    pd.testing.assert_series_equal(float_series, expected, atol=.005)


def test_dataframe_ignore_order():
    """Test whether DataFrames match ignoring row and column order."""
    data = pd.DataFrame({
        "x": [4, 2, 3, 1],
        "y": [1, 0, 1, 0],
    })

    # Re-order rows and columns.
    expected = data.sort_values("x")[["y", "x"]]

    # Test equality using check_like.
    # Note: row and column order is ignored!
    pd.testing.assert_frame_equal(data, expected, check_like=True)
