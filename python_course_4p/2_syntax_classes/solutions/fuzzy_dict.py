import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercises 4 : Solutions
    """)
    return


@app.class_definition
class FuzzyDict:
    """Dict-class that is case insensitive."""

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        """Get a key from the data."""
        key = key.lower().strip()
        return self.data[key]

    def __setitem__(self, key, value):
        """Set a key in the data."""
        key = key.lower().strip()
        self.data[key] = value

    def __str__(self):
        """String representation of the data."""
        return str(self.data)
    
    def __len__(self):
        """Return the number of key-value pairs."""
        return len(self.data)

    def keys(self):
        """Map keys method to data dict."""
        return self.data.keys()

    def values(self):
        """Map values method to data dict."""
        return self.data.values()


@app.cell
def _():
    # Initialize a FuzzyDict object.
    fuzzydict = FuzzyDict()
    return (fuzzydict,)


@app.cell
def _(fuzzydict):
    # Store name using lowercase key.
    fuzzydict["name"] = "John Doe"
    return


@app.cell
def _(fuzzydict):
    # Check using original lowercase key.
    # Should return "John Doe".
    fuzzydict["name"]
    return


@app.cell
def _(fuzzydict):
    # Check using uppercase key.
    # Should return "John Doe" as well.
    fuzzydict["NAME"]
    return


@app.cell
def _(fuzzydict):
    # Store using uppercase key, then retrieve with lowercase key.
    # Should return "Jane Doe".
    fuzzydict["NAME"] = "Jane Doe"
    fuzzydict["name"]
    return


@app.cell
def _(fuzzydict):
    # String representation.
    print(fuzzydict)
    return


@app.cell
def _(fuzzydict):
    # Get the dict keys.
    fuzzydict.keys()
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
