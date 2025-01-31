# File: src/strategies/example_strategy.py
import pandas as pd


def moving_average_crossover_strategy(df, price_col="Close", short_window=10, long_window=50):
    """
    Enhanced MA crossover strategy with position tracking
    Returns DataFrame with:
    - signal: 1 (long), -1 (short), 0 (neutral)
    - position: Changes in positions (1=enter long, -1=exit long, etc.)
    """
    # Validate input
    if price_col not in df.columns:
        raise ValueError(f"Price column '{price_col}' not found in DataFrame")

    if len(df) < long_window:
        raise ValueError(f"Need at least {long_window} data points for strategy calculation")

    # Calculate moving averages
    df = df.copy()
    df["SMA_short"] = df[price_col].rolling(window=short_window).mean()
    df["SMA_long"] = df[price_col].rolling(window=long_window).mean()

    # Generate signals
    df["signal"] = 0
    df.loc[df["SMA_short"] > df["SMA_long"], "signal"] = 1
    df.loc[df["SMA_short"] < df["SMA_long"], "signal"] = -1

    # Identify position changes
    df["position"] = df["signal"].diff().fillna(0)

    # Clean up position values
    df['position'] = df['position'].astype(int)

    return df