import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import requests

    return mo, requests


@app.cell
def _():
    host = "http://localhost:8000/"
    return (host,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Path Parameters
    """)
    return


@app.cell
def _(host, requests):
    path_response = requests.get(host + "greet/John/Doe")
    path_response
    return (path_response,)


@app.cell
def _(path_response):
    path_response.text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Query parameters
    """)
    return


@app.cell
def _(host, requests):
    query_response = requests.get(host + "hello?name=John&last_name=Doe")
    query_response.text
    return


@app.cell
def _(host, requests):
    param_response = requests.get(host + "hello", params={"name": "John", "last_name": "Doe"})
    param_response.text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Request Body
    """)
    return


@app.cell
def _():
    user = {
        "name": "John",
        "last_name": "Doe",
    }
    return (user,)


@app.cell
def _(host, requests, user):
    body_response = requests.post(host + "wave", json=user)
    body_response.text
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
