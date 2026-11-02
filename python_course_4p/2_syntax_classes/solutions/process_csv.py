"""Module for processing personal data."""

# Define filename as constant.
INPUT_FILE = "../exercises/personal_data.csv"


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
    with open(input_path, "r", encoding="utf-8") as data_file:

        # Use first line as header.
        # Note: Need strip() for EOL (\n) character.
        header = next(data_file).strip().split(",")

        for line in data_file:
            # Read a record, split values.
            record = line.strip().split(",")

            # Create dict linking header and record values.
            dict_record = {}
            for idx, field in enumerate(header):
                dict_record[field] = record[idx]

            # Alternative:
            # Use zip to create (header, value) tuples then cast to dict.
            # dict_record = dict(zip(header, record))

            data.append(dict_record)

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
    result = []

    # Split names into separate words.
    for part in name.split():

        # Keep first character, replace rest with "*".
        masked = part[0] + "*" * (len(part) - 1)
        result.append(masked)

    # Rejoin words.
    return " ".join(result)


def main():
    """Read input data, compute factorials and write output data."""

    print(f"Reading input data from: {INPUT_FILE}")
    data = read_csv(INPUT_FILE)

    print(f"Anonymize the names for {len(data)} persons.")
    for person in data:
        person["name"] = anonymize_name(person["name"])

    print(data)



if __name__ == "__main__":
    main()
