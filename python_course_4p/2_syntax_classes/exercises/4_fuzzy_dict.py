import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    # Exercises 4
    return


@app.class_definition
class FuzzyDict:
    """Dict-class that is case insensitive."""

    def __init__(self):
        """Constructor; create dict to hold the data."""
        self.data = {}

    def __getitem__(self, key):
        """Get a key from the data."""
        # Your code here...

    def __setitem__(self, key, value):
        """Set a key in the data."""
        # Your code here...


@app.cell
def _():
    # Initialize a FuzzyDict object
    fuzzydict = FuzzyDict()
    return (fuzzydict,)


@app.cell
def _(fuzzydict):
    # Store name using lowercase key
    fuzzydict["name"] = "John Doe"
    return


@app.cell
def _(fuzzydict):
    # Retrieve using lowercase key
    fuzzydict["name"]
    return


@app.cell
def _(fuzzydict):
    # Check using uppercase key
    # Should return "John Doe"
    fuzzydict["NAME"]
    return


if __name__ == "__main__":
    app.run()
