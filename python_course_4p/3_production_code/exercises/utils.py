"""Module for utility functions."""


def mean(values, fillna=0):
    """Compute mean for a list of numeric values.

    Parameters
    ----------
    values : list
        List of numeric values.
    fillna : int or float, default=0
        Replace None values with this number, defaults to 0.

    Returns
    -------
    float
        Mean for the provided values.

    Raises
    ------
    TypeError
        Raised when values are not numeric.
    ValueError
        Raised when list is empty.
    """
    try:
        filled = [fillna if v is None else v for v in values]
        return sum(filled) / len(filled)

    except TypeError as error:
        raise TypeError("List contains non-numeric values.") from error

    except ZeroDivisionError as error:
        raise ValueError("List of values is empty.") from error
