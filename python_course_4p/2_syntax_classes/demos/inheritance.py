import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Inheritance
    """)
    return


@app.class_definition
class TextReader:
    """Class for reading text data."""

    def __init__(self, file_path):
        print("Called __init__ from TextReader.")
        self.path = file_path

    def read(self):
        """Read text file and return lines as list."""
        print("Called read() from TextReader")
        with open(self.path, "r") as dfile:
            return [line.strip() for line in dfile]


@app.class_definition
class CSVReader(TextReader):
    """Class for reading CSV data."""

    def __init__(self, path, separator):
        # Calling constructor from TextData.
        print("Called __init__ from CSVReader")
        super().__init__(path)
        self.separator = separator

    def read(self):
        """Read CSV file and return data as list of lists."""
        print("Called read() from CSVReader")
        return [
            line.split(self.separator)
            for line in super().read()
        ]


@app.cell
def _():
    # Construct TextReader object.
    text_reader = TextReader("exercises/personal_data.csv")
    return (text_reader,)


@app.cell
def _():
    # Construct CSVReader object.
    # Note: Calls constructor of TextReader using super().
    csv_reader = CSVReader("exercises/personal_data.csv", ",")
    return (csv_reader,)


@app.cell
def _(text_reader):
    # Reading data as text.
    text_reader.read()
    return


@app.cell
def _(csv_reader):
    # Reading data as CSV
    csv_reader.read()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Type and isinstance
    """)
    return


@app.cell
def _(csv_reader, text_reader):
    # Type gives the actual class name
    print("TextReader:   ", type(text_reader))
    print("CSVReader:    ", type(csv_reader))
    return


@app.cell
def _(text_reader):
    # As expected, text_reader is a TextReader instance
    isinstance(text_reader, TextReader)
    return


@app.cell
def _(csv_reader):
    # And csv_reader a CSVReader instance...
    isinstance(csv_reader, CSVReader)
    return


@app.cell
def _(csv_reader):
    # But... csv_reader is also a TextReader instance!
    isinstance(csv_reader, TextReader)
    return


@app.cell
def _(csv_reader):
    # Using type() for strict checking.
    type(csv_reader) == CSVReader
    return


@app.cell
def _(csv_reader):
    # Using type() for strict checking.
    type(csv_reader) == TextReader
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
