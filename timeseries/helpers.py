import math

import numpy as np
import pandas as pd
import altair as alt

from sktime.forecasting.arima import ARIMA


def generate_random_walk(n: int, step: int = 1, intercept: float = 0.0):
    """Generator for a random walk time series.

    Parameters
    ----------
    n : int
        Length of the time series.
    step : int, default=1
        Maximum step size for each change, by default 1.
    intercept : float, default=0.0
        Starting value of the time series, by default 0.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    choices = list(range(-step, step + 1))
    changes = np.random.choice(choices, size=n).cumsum()
    return pd.Series(intercept + changes)


def generate_autoregression(
    n: int, coef: float = 0.9, intercept: float = 0.0, noise: tuple = (0, 1)
):
    """Generate a time series with autoregressive trend.

    Parameters
    ----------
    n : int
        Length of the time series.
    coef : float, default=0.9
        Coefficient for the autoregressive trend, by default 0.9.
    intercept : float, default=0.0
        Intercept for the time series, by default 0.0.
    noise : tuple, default=(0, 1)
        Mean and standard deviation for the series noise.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    # Generate noise unless turned off.
    if noise:
        y = np.random.normal(noise[0], noise[1], size=n)
    else:
        y = [0] * n

    # Generate auto-correlation using specified coefficient.
    for i in range(len(y)):
        if i > 0:
            y[i] += coef * y[i-1]

    return intercept + pd.Series(y)


def generate_linear(n: int, slope: float = 1.0, intercept: float = 0.0):
    """Generate a time series with a linear trend.

    Parameters
    ----------
    n : int
        Length of the time series.
    slope : float, default=1.0
        Slope of the linear trend, by default 1.0.
    intercept : float, default=0.0
        Intercept of the linear trend, by default 0.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    return pd.Series([intercept + _ * slope for _ in range(n)])


def generate_exponential(n: int, exponent: float = 1.05, intercept: float = 0.0):
    """Generate a time series with an exponential trend.

    Parameters
    ----------
    n : int
        Length of the time series.
    exponent : float, default=1.05
        Base of the exponential trend, by default 1.05.
    intercept : float, default=0.0
        Intercept of the exponential trend, by default 0.0

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    return pd.Series([intercept + exponent**_ for _ in range(n)])


def generate_sigmoid(
    n: int, exponent: float = 1.05, scale: float = 1.0, intercept: float = 0.0
):
    """Generate a time series with a sigmoid trend.

    Parameters
    ----------
    n : int
        Length of the time series.
    exponent : float, default=1.05
        Exponent for the sigmoid function, by default 1.05.
    scale : float, default=1.0
        Scaling factor for the sigmoid trend, by default 1.0.
    intercept : float, default=0.0
        Intercept of the sigmoid trend, by default 0.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    x = np.linspace(-10, 10, n)
    return intercept + pd.Series(1 / (1 + exponent**-x)) * scale


def generate_sine(
    n: int, amplitude: float = 1.0, frequency: float = 1.0, phase: float = 0.0
):
    """Generate a time series with a sine trend.

    Parameters
    ----------
    n : int
        Length of the time series.
    amplitude : float, default=1.0
        Amplitude of the sine wave, by default 1.0.
    frequency : float, default=1.0
        Frequency of the sine wave, by default 1.0.
    phase : float, default=0.0
        Phase shift of the sine wave, by default 0.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series.
    """
    x = np.linspace(0, 2 * np.pi * frequency, n)
    return pd.Series(amplitude * np.sin(x + phase * math.pi))


def add_linear(series: pd.Series, slope: float, intercept: float = 0.0):
    """Add a linear trend to a time series.

    Parameters
    ----------
    series : pd.Series
        The original time series to which the linear trend will be added.
    slope : float
        The slope of the linear trend.
    intercept : float, default=0.0
        The intercept of the linear trend, by default 0.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series with the added linear trend.
    """
    linear = generate_linear(len(series), slope=slope, intercept=intercept)
    return series + linear


def add_seasonality(series: pd.Series, pattern: list, scale: float = 1.0):
    """Add a seasonal pattern to a time series.

    Parameters
    ----------
    series : pd.Series
        The original time series to which the seasonal pattern will be added.
    pattern : list
        A list representing the seasonal pattern.
    scale : float or list, default=1.0
        Scaling factor or (min, max) range for the seasonal pattern.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series with the added seasonal pattern.
    """
    seasonality = pd.Series([pattern[_ % len(pattern)] for _ in range(len(series))])

    if isinstance(scale, (list, tuple)):
        scale = np.linspace(scale[0], scale[1], len(series))

    return series + seasonality * scale


def add_noise(series: pd.Series, sd: float = 1.0):
    """Add random noise to a time series.

    Parameters
    ----------
    series : pd.Series
        The original time series to which noise will be added.
    sd : float, default=1.0
        Standard deviation of the noise to be added, by default 1.0.

    Returns
    -------
    pd.Series
        A pandas Series representing the time series with added noise.
    """
    noise = np.random.normal(0, sd, len(series))
    return series + noise


def plot_timeseries(
    series: dict,
    colors: dict = None,
    mark: str = "line",
    title: str = None,
    properties: dict = None,
    config: dict = None,
):
    """Plot a time series using Altair.

    Parameters
    ----------
    series : pandas.Series, list or dict
        A Series, list or a dict of names and series to be plotted.
        Note: Add "Time" as a key to use it as x-axis.
    colors : str or dict, default None.
        A color or a dict of names and colors for each timeseries.
    mark : {"line", "bar"}, default="line"
        Type of the chart to be plotted, by default "line".
    title : str, optional
        Title for the chart, by default None.
    properties : dict, optional
        Additional properties for the Altair chart, by default None.
    config : dict, optional
        Configuration for the Altair chart, by default None.

    Returns
    -------
    alt.Chart
        An Altair chart object representing the time series.
    """
    # Plot single or multiple time series.
    if isinstance(series, pd.Series) == 1:
        yname = series.name or "Timeseries"
        df = pd.DataFrame({"Time": series.index, yname: series})

        if isinstance(colors, str):
            plot = alt.Chart(df).encode(x="Time", y=yname, color=alt.value(colors))
        else:
            plot = alt.Chart(df).encode(x="Time", y=yname)

    elif isinstance(series, list):
        df = pd.DataFrame(
            {
                "Time": range(len(series)),
                "Timeseries": series,
            }
        )

        if isinstance(colors, str):
            plot = alt.Chart(df).encode(
                x="Time", y="Timeseries", color=alt.value(colors)
            )
        else:
            plot = alt.Chart(df).encode(x="Time", y="Timeseries")

    elif isinstance(series, dict):
        df = pd.DataFrame(series)
        if "Time" not in df.columns:
            df["Time"] = df.index
        df = df.melt(id_vars="Time", var_name="Series", value_name="Value")

        if isinstance(colors, dict):
            colors = alt.Color(
                "Series", scale=alt.Scale(domain=colors.keys(), range=colors.values())
            )
        else:
            colors = "Series:N"
        plot = alt.Chart(df).encode(x="Time", y="Value", color=colors)

    else:
        raise ValueError("Series must be pandas.Series, list or dict.")

    if mark == "bar":
        plot = plot.mark_bar()
    else:
        plot = plot.mark_line(point=True)

    # Set properties for the chart
    actual_props = properties or {}
    actual_props["title"] = title or ""
    plot = plot.properties(**actual_props)

    # Set configuration for the chart
    if config:
        plot = plot.configure(**config)

    return plot


def plot_forecaster(
    series: pd.Series | list,
    forecaster: ARIMA,
    colors: dict = None,
    plot_horizon: int | list | None = None,
    properties: dict = None,
    title: str = None,
):
    """Plot time series and forecast."""
    if isinstance(plot_horizon, int):
        plot_horizon = [_ + 1 for _ in range(plot_horizon)]
    colors = colors or {}

    # Create the plots.
    plot = plot_timeseries(series, colors=colors.get("values"))

    # Plot forecasting horizon.
    if plot_horizon:
        plot += plot_timeseries(
            forecaster.predict(fh=plot_horizon), colors=colors.get("forecast")
        )

        quantiles = forecaster.predict_interval(fh=plot_horizon, coverage=0.90)
        quantiles.columns = ["lower", "upper"]
        quantiles["Time"] = quantiles.index

        plot += (
            alt.Chart(quantiles)
            .mark_errorband()
            .encode(
                alt.X("Time"),
                alt.Y("lower", title="Timeseries"),
                alt.Y2("upper"),
            )
        )

    actual_props = properties or {}
    actual_props["title"] = title or ""
    plot = plot.properties(**actual_props)

    return plot
