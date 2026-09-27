import marimo

__generated_with = "0.25.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercises 2: Solutions
    """)
    return


@app.cell
def _():
    # Define filename as constant.
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
        with open(input_path, "r", encoding="utf-8") as data_file:

            # Use first line as header.
            # Note: Need strip() for EOL (\n) character.
            header = next(data_file).strip().split(",")

            for line in data_file:
                # Read record values.
                record = line.strip().split(",")

                # Zip to creates [(header, value), ..., (header, value)] pairs.
                # Then casting tuple pairs to dict.
                record = dict(zip(header, record))
                data.append(record)

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
    return


if __name__ == "__main__":
    app.run()
