import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib

    return (pd,)


@app.cell
def _():
    nrs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (nrs,)


@app.cell
def _():
    power = 1
    return (power,)


@app.cell
def _(nrs, power):
    y = [n ** power for n in nrs]
    return (y,)


@app.cell
def _(nrs, pd, y):
    df = pd.DataFrame({"x": nrs, "y": y})
    return (df,)


@app.cell
def _(df):
    df.plot(x="x", y="y")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
