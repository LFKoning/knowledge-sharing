import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import logging

    import marimo as mo

    return logging, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Logger objecten
    """)
    return


@app.cell
def _(logging):
    # Using getLogger() without a name returns the root logger.
    # Note: logging level defaults to logging.WARNING.
    root_logger = logging.getLogger()
    root_logger
    return (root_logger,)


@app.cell
def _(logging):
    # Create your own named logger.
    # Note: Root logger is the parent.
    test_logger = logging.getLogger("TestLogger")
    test_logger
    return (test_logger,)


@app.cell
def _(test_logger):
    # Use methods on the logger to produce log messages.
    test_logger.warning("Hello World!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Logging format
    """)
    return


@app.cell
def _():
    # Define a logging format using formatting strings.
    root_fmt = "%(asctime)s | %(levelname)-8s | %(name)-10s | %(message)-40s"
    return (root_fmt,)


@app.cell
def _(logging, root_fmt):
    # Apply a format to the root logger using basicConfig.
    # Note: Use datefmt argument to set format for asctime.
    logging.basicConfig(
        format=root_fmt,
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.INFO,
    )
    return


@app.cell
def _(logging):
    # Logging directly through the root logger.
    logging.info("First message from ROOT.")
    logging.warning("Second message from ROOT.")
    return


@app.cell
def _(test_logger):
    # Logging through test_logger.
    # Note: Output goes through root, but logger name changed.
    test_logger.info("First message from TestLogger.")
    test_logger.warning("Second message for TestLogger.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Handlers en Formatters
    """)
    return


@app.cell
def _(root_logger):
    # Root logger gets a StreamHandler after basicConfig() or logging a message.
    root_logger.handlers
    return


@app.cell
def _(test_logger):
    # The test_logger has no handlers; it produces no output.
    test_logger.handlers
    return


@app.cell
def _(logging):
    # Handlers in the logging module.
    for _ in dir(logging):
        if _.endswith("Handler") and not _.startswith("_"):
            print(_)
    return


@app.cell
def _(logging):
    # Handlers in the logging.handlers module.
    for _ in dir(logging.handlers):
        if _.endswith("Handler"):
            print(_)
    return


@app.cell
def _(logging, test_logger):
    # Create a FileHandler for our test_logger.
    file_handler = logging.FileHandler("test_logger.csv")
    test_logger.addHandler(file_handler)

    # Note that test_logger now has its own handler.
    test_logger.handlers
    return (file_handler,)


@app.cell
def _(test_logger):
    # Log a message using TestLogger.
    # Note: Output from root and file from TestLogger.
    test_logger.info("Message from TestLogger")
    return


@app.cell
def _(logging):
    # Create a Formatter for a proper CSV format.
    csv_formatter = logging.Formatter(
        fmt="%(asctime)s,%(levelname)s,%(name)s,%(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
    )
    return (csv_formatter,)


@app.cell
def _(csv_formatter, file_handler):
    # Set file_handler from test_logger to the CSV format.
    file_handler.setFormatter(csv_formatter)
    return


@app.cell
def _(test_logger):
    # Log using the new format.
    test_logger.info("Another message from TestLogger")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
