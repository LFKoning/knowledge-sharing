"""Module for processing personal data."""

# Define filenames as constants
INPUT_FILE = "../../0_data/persons/personal_data.csv"
OUTPUT_FILE = "output.csv"


def read_input(input_path):
    """Read input CSV data from the provided path.

    Parameters
    ----------
    input_path : str
        Path to the input data file as string.

    Returns
    -------
    list
        Data as a list of dicts.
    """
    # Open the file and process lines into records.
    # Note: Watch the data types!


def write_output(output_path, data):
    """Write data to the provided path.

    Parameters
    ----------
    output_path : str
        Path to the output file as string.
    data : list
        Data as a list of dicts.
    """
    # Write header for the CSV file.
    # Write record(s) to the CSV file.


def md5_hash(name):
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



    print(f"Writing output to: {OUTPUT_FILE}")
    write_output(OUTPUT_FILE, data)


if __name__ == "__main__":
    main()
