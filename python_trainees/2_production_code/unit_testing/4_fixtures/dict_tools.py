"""Module for dict helper functions."""


def recursive_update(new_values, old_values):
    """Recursively update one dict with another.

    Parameters
    ----------
    new_values : dict
        New values to update old ones with.
    old_values : dict
        Old values to be overwritten.

    Returns
    -------
    dict
        Dict with updated values.
    """

    for key in new_values:

        # Existing key: recursively combine.
        if (
            key in old_values
            and isinstance(old_values[key], dict)
            and isinstance(new_values[key], dict)
        ):
            recursive_update(old_values[key], new_values[key])

        # New key: simply add.
        else:
            old_values[key] = new_values[key]

    # Return the updated values
    return old_values
