import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import requests

    return (requests,)


@app.cell
def _():
    API_URL = "http://localhost:8000"
    return (API_URL,)


@app.cell
def _(API_URL, requests):
    # Call the list endpoint without any parameters.
    response = requests.get(url=f"{API_URL}/list", timeout=5)
    response.status_code
    return (response,)


@app.cell
def _(response):
    # View response as text.
    response.text
    return


@app.cell
def _(response):
    # Parse response as JSON string.
    response.json()
    return


@app.cell
def _(API_URL, requests):
    # Use parameters to filter tasks.
    filtered = requests.get(url=f"{API_URL}/list", params={"status": "Completed"}, timeout=5)
    filtered.status_code
    return (filtered,)


@app.cell
def _(filtered):
    filtered.json()
    return


@app.cell
def _(API_URL, requests):
    # Error on incorrect parameter value.
    error = requests.get(url=f"{API_URL}/list", params={"priority": "Invalid"}, timeout=5)
    error.status_code
    return (error,)


@app.cell
def _(error):
    # Get information on the error.
    error.json()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
