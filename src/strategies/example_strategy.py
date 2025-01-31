def moving_average_crossover_strategy(df, price_col="Close", short_window=10, long_window=50):
    """
    Implements a simple moving average crossover strategy.
    :param df: The input DataFrame.
    :param price_col: The name of the price column to use (default: 'Close').
    :param short_window: The window size for the short moving average.
    :param long_window: The window size for the long moving average.
    :return: A DataFrame with signals for trading.
    """

    # Ensure the price column exists
    if price_col not in df.columns:
        raise ValueError(f"Column '{price_col}' not found in DataFrame")

    # Calculate short and long simple moving averages
    df["SMA_short"] = df[price_col].rolling(window=short_window).mean()
    df["SMA_long"] = df[price_col].rolling(window=long_window).mean()

    # Generate signals: 1 = buy, -1 = sell
    df["signal"] = 0
    df.loc[df["SMA_short"] > df["SMA_long"], "signal"] = 1
    df.loc[df["SMA_short"] < df["SMA_long"], "signal"] = -1

    return df
