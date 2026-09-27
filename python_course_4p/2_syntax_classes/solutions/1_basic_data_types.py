import marimo

__generated_with = "0.25.0"
app = marimo.App()


@app.cell
def _():
    # Exercises 1 : Solutions
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
    # Note: Does not result in 3 like int(3.7) does.
    print(f"Convert string {s!r} to int: ", int(s))
    return


@app.cell
def _():
    # String multiplication just repeats the string.
    # Note: Does not try to convert "123" to numeric.
    "123" * 3
    return


@app.cell
def _():
    # List multiplication.
    # Note: Does not multiply the elements!
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
    return


if __name__ == "__main__":
    app.run()
