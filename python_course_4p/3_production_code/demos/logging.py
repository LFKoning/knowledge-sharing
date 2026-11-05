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
    log_fmt = "%(asctime)s | %(levelname)-8s | %(name)-10s | %(message)-40s"
    return (log_fmt,)


@app.cell
def _(log_fmt, logging):
    # Apply a format to the root logger using basicConfig.
    # Note: Use datefmt argument to set format for asctime.
    logging.basicConfig(
        format=log_fmt,
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
    # Logging through custom test_logger.
    # Note: Identical, because output goes through the root logger.
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
    # Create a StreamHandler and add it to test_logger.
    test_handler = logging.StreamHandler()
    test_logger.addHandler(test_handler)

    # Note that test_logger now has its own handler.
    test_logger.handlers
    return (test_handler,)


@app.cell
def _(test_logger):
    # Log a message using test_logger.
    # Note: Output from both root and test_logger.
    test_logger.info("Message from TestLogger")
    return


@app.cell
def _(logging):
    # Create a Formatter using a CSV format.
    csv_format = "%(asctime)s,%(levelname)s,%(name)s,%(message)s"
    csv_formatter = logging.Formatter(csv_format, datefmt="%d-%m-%Y %H:%M:%S")
    return (csv_formatter,)


@app.cell
def _(csv_formatter, test_handler):
    # Set handler of test_logger to csv_formatter.
    test_handler.setFormatter(csv_formatter)
    return


@app.cell
def _(test_logger):
    # Log using the new format.
    test_logger.info("Message from TestLogger")
    return


@app.cell
def _(csv_formatter, logging):
    # Create a FileHandler using the CSV Formatter.
    file_handler = logging.FileHandler("test_logger.csv")
    file_handler.setFormatter(csv_formatter)
    return (file_handler,)


@app.cell
def _(file_handler, test_logger):
    # Add the file_handler to test_logger.
    test_logger.addHandler(file_handler)

    # Note: test_logger now has 2 handlers.
    test_logger.handlers
    return


@app.cell
def _(test_logger):
    # Log a few messages.
    test_logger.info("Info message from TestLogger.")
    test_logger.warning("Warning message from TestLogger")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
