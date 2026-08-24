"""Module for processing personal data."""

# Define filename as constant
INPUT_FILE = "../../0_data/persons/personal_data.csv"


def read_csv(input_path):
    """Read CSV data from the provided path.

    Parameters
    ----------
    input_path : str
        Path to the input data file as string.

    Returns
    -------
    list
        Data as a list of dicts.
    """
    data = []

    # Parse CSV data into a list of dicts using this format:
    # {"name": "...", "gender": "...", "age": ...}

    return data


def anonymize_name(name):
    """Anonymize names by masking them with *.

    Parameters
    ----------
    name : str
        Name to anonymize.

    Returns
    -------
    str
        Name masked with *.
    """

    # Mask names with * using this format:
    # "John Doe" becomes "J*** D**".

    return name


def main():
    """Read input data, compute factorials and write output data."""

    print(f"Reading input data from: {INPUT_FILE}")
    data = read_csv(INPUT_FILE)

    print(f"Anonymizing names for {len(data)} persons.")
    for person in data:
        person["name"] = anonymize_name(person["name"])

    print(data)


if __name__ == "__main__":
    main()
