# File: src/main.py

import pandas as pd
from src.data.data_handler import load_and_clean_data
from src.strategies.example_strategy import moving_average_crossover_strategy


def main():
    # 1. Load the CSV into a DataFrame
    filepath = "data/historical/AAPL_2024-01-01_to_2025-01-28.csv"
    df = load_and_clean_data(filepath)  # from data_handler.py

    # 2. Apply the strategy
    df = moving_average_crossover_strategy(df)

    # 3. Preview the signals
    print(df[["Close", "SMA_short", "SMA_long", "signal"]].head(200))


if __name__ == "__main__":
    main()
