"""Module for utility functions."""

def mean(values, dropna=False):
    """Compute mean for a list of numeric values.

    Parameters
    ----------
    values : list
        List of numeric values.
    dropna : bool, default=False
        Omit missing values in copmputing the mean.

    Returns
    -------
    float
        Mean value for the provided values.

    Raises
    ------
    TypeError
        Raised when values are not numeric.
    ValueError
        Raised when list is empty.
    """
    try:
        filtered = [v for v in values if v is not None]
        if dropna:
            return sum(filtered) / len(filtered)
        return sum(filtered) / len(values)

    except TypeError as error:
        raise TypeError("List contains non-numeric values.") from error

    except ZeroDivisionError as error:
        raise ValueError("List of values is empty.") from error


def absmean(values, dropna=False):
    """Compute absolute mean for a list of numeric values.

    Parameters
    ----------
    values : list
        List of numeric values.
    dropna : bool, default=False
        Omit missing values in copmputing the mean.

    Returns
    -------
    float
        Mean value for the provided values.

    Raises
    ------
    TypeError
        Raised when values are not numeric.
    ValueError
        Raised when list is empty.
    """
    try:
        absolutes = [v if v >=0 else -1 * v for v in values]
    except TypeError as error:
        raise TypeError("List contains non-numeric values.") from error

    return mean(absolutes, dropna)
