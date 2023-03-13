"""Module containing helper functions."""


def mean(numbers: list, dropna=False) -> float:
    """Compute the mean for a list of numbers"""

    # Check input is list or tuple
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Numbers must be provided as a list or tuple.")

    # Check validity of provided numbers
    valid = []
    for number in numbers:
        if number is None:
            continue

        try:
            number = float(number)
        except ValueError:
            raise ValueError("Cannot compute mean for non-numeric input.")

        valid.append(number)

    # When dropping missings, count valid only
    count = len(valid) if dropna else len(numbers)

    return sum(valid) / count
