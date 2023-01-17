"""Module for dict helper functions."""


def recursive_update(new, old):
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
    keys = set(new) | set(old)

    # Create a new dict.
    updated = {}

    # Then copy the values into it.
    for key in keys:
        if key in new:
            if (
                key in old
                and isinstance(new[key], dict)
                and isinstance(old[key], dict)
            ):
                updated[key] = recursive_update(new[key], old[key])
            else:
                updated[key] = new[key]
        else:
            updated[key] = old[key]

    # Return the updated values.
    return updated
