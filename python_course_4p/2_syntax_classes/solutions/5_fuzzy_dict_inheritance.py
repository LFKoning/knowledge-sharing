import marimo

__generated_with = "0.25.0"
app = marimo.App()


@app.cell
def _():
    # Exercises 5 : Solutions
    return


@app.cell
def _():
    from collections import UserDict


    class FuzzyDict(UserDict):
        """Dict-class that is case insensitive."""

        def __getitem__(self, key):
            """Get a key from the data."""
            key = key.lower().strip()
            return super().__getitem__(key)

        def __setitem__(self, key, value):
            """Set a key in the data."""
            key = key.lower().strip()
            super().__setitem__(key, value)

    return FuzzyDict, UserDict


@app.cell
def _(FuzzyDict):
    # Create an empty FuzzyDict instance.
    fd = FuzzyDict()
    return (fd,)


@app.cell
def _(fd):
    # Test setting a key...
    fd["NAAM"] = "Henk"
    return


@app.cell
def _(fd):
    # Inhrited keys() method from UserDict
    fd.keys()
    return


@app.cell
def _(fd):
    # But... not entirely fuzzy :-(
    print("Lower case: ", "naam" in fd)
    print("Upper case: ", "NAAM" in fd)
    return


@app.cell
def _(UserDict):
    class FuzzyDict_1(UserDict):
        """Dict-class that is case insensitive."""

        def __getitem__(self, key):
            """Get a key from the data."""
            key = key.lower().strip()
            return super().__getitem__(key)

        def __setitem__(self, key, value):
            """Set a key in the data."""
            key = key.lower().strip()
            super().__setitem__(key, value)

        def __contains__(self, key):
            """Check key is in the dict."""
            key = key.lower().strip()
            return super().__contains__(key)

    return (FuzzyDict_1,)


@app.cell
def _(FuzzyDict_1):
    # Create an empty FuzzyDict instance.
    fd_1 = FuzzyDict_1()
    fd_1['NAAM'] = 'Henk'
    return (fd_1,)


@app.cell
def _(fd_1):
    # Truly fuzzy!
    print('Lower case: ', 'naam' in fd_1)
    print('Upper case: ', 'NAAM' in fd_1)
    return


@app.cell
def _(FuzzyDict_1):
    # Alternative construction method, inherited from UserDict
    # Note: All keys lower cased, constructor uses custom __setitem__.
    FuzzyDict_1({'A': 1, 'b  ': 2, ' C': 3})
    return


if __name__ == "__main__":
    app.run()
