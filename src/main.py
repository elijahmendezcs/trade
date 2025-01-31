# File: src/main.py
import pandas as pd
from src.data.data_handler import load_and_clean_data
from src.strategies.example_strategy import moving_average_crossover_strategy


def main():
    try:
        # 1. Load data
        filepath = "data/historical/AAPL_2000-01-01_to_2025-01-28.csv"
        df = load_and_clean_data(filepath)

        # 2. Apply strategy
        df = moving_average_crossover_strategy(df)

        # 3. Filter and format signals
        signals = df[["Close", "SMA_short", "SMA_long", "signal", "position"]]
        signals = signals[signals['position'] != 0]  # Only show actual trades

        # 4. Print formatted results
        print("\n" + "=" * 50)
        print(f"Trading Signals ({len(signals)} events found)")
        print("=" * 50)

        if not signals.empty:
            for index, row in signals.iterrows():
                action = "BUY" if row['position'] > 0 else "SELL"
                print(f"{index.date()} | Price: ${row['Close']:.2f} | "
                      f"Short MA: {row['SMA_short']:.2f} | Long MA: {row['SMA_long']:.2f} | "
                      f"Action: {action} ({'Entry' if abs(row['position']) == 1 else 'Exit'})")
        else:
            print("No trading signals generated!")
            print("Possible reasons:")
            print("- Insufficient data for MA calculations")
            print("- No crossover events in the period")
            print("- Check your CSV file has enough historical data")

        # 5. Data validation
        required_bars = max(10, 50 + 1)  # Long window + 1
        if len(df) < required_bars:
            print(f"\nWarning: Only {len(df)} bars in data. Need at least {required_bars} "
                  "for reliable signals")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()