import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercises 1 : Solutions
    """)
    return


@app.cell
def _():
    f = 3.7
    s = "3.7"
    return f, s


@app.cell
def _(f):
    # float => int: simply drops decimals.
    print(f"Convert float {f} to int: ", int(f))
    return


@app.cell
def _(s):
    # str => float: succeeds on valid values.
    print(f"Convert string {s!r} to float: ", float(s))
    return


@app.cell
def _(s):
    # str => int: ValueError on invalid values.
    # Note: Does not work like int(3.7).
    print(f"Convert string {s!r} to int: ", int(s))
    return


@app.cell
def _():
    # String multiplication repeats the string.
    # Note: Does force conversion of "123" to numeric.
    "123" * 3
    return


@app.cell
def _():
    # List multiplication.
    # Note: Does not multiply elementwise!
    [1, 2, 3] * 3
    return


@app.cell
def _():
    # Initialize a matrix...
    zeroes = [[0] * 3] * 3
    zeroes
    return (zeroes,)


@app.cell
def _(zeroes):
    # Maybe not the best way...
    zeroes[0][0] = 1
    zeroes
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
