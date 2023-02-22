"""Module containing code for the first exercise"""

# Define filenames as constants
INPUT_FILE = "data.csv"
OUTPUT_FILE = "output.csv"


def read_input(input_path):
    """Read input CSV data from the provided path.

    Parameters
    ----------
    input_path : str
        Path to the input data as string.

    Returns
    -------
    list
        Data as a list of dicts
    """
    data = []
    with open(input_path, "r", encoding="utf8") as data_file:
        for line in data_file:
            name, gender, age = line.split(",")
            data.append(
                # Age needs to be converted from string to integer
                {"name": name, "gender": gender, "age": int(age)}
            )

    return data


def write_output(output_path, data):
    """Write data to the provided path.

    Warning: Overwrites the output file if it exists!

    Parameters
    ----------
    output_path : str
        Path to the output file as string.
    data : list
        Data as a list of dicts.
    """
    template = "{name},{gender},{age},{age_factorial}\n"

    with open(output_path, "w", encoding="utf8") as output_file:
        for record in data:
            # Format dict records into a string
            output_file.write(template.format(**record))


def compute_factorial(age):
    """Computes factorial for the provided aga.

    Parameters
    ----------
    age : int
        Age to compute factorial for as integer.

    Returns
    -------
    int
        Factorial for the provided age.
    """
    factorial = 1
    for x in range(age):
        factorial *= (x + 1)
    return factorial


def main():
    """Read input data, compute factorials and write output data."""

    print(f"Reading input data from: {INPUT_FILE}")
    data = read_input(INPUT_FILE)

    print(f"Computing factorial of age for {len(data)} persons.")
    for person in data:
        person["age_factorial"] = compute_factorial(person["age"])

    print(f"Writing output to: {OUTPUT_FILE}")
    write_output(OUTPUT_FILE, data)


if __name__ == "__main__":
    main()
