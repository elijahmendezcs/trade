import os
import yfinance as yf
import pandas as pd

def fetch_historical_data(symbol, start_date, end_date, save_dir="data/historical"):
    """
    Fetch historical stock data using yfinance and save it as a CSV file.
    :param symbol: Stock ticker symbol (e.g., 'AAPL').
    :param start_date: Start date (YYYY-MM-DD).
    :param end_date: End date (YYYY-MM-DD).
    :param save_dir: Directory to save the CSV file.
    """
    print(f"Fetching data for {symbol} from {start_date} to {end_date}...")

    # Ensure save directory exists
    os.makedirs(save_dir, exist_ok=True)

    try:
        data = yf.download(symbol, start=start_date, end=end_date)

        if data.empty:
            print(f"No data available for {symbol}")
            return

        # If we have multi-level columns, flatten them.
        if hasattr(data.columns, "nlevels") and data.columns.nlevels > 1:
            data.columns = [
                "_".join(col).strip() for col in data.columns.to_flat_index()
            ]

        # Write CSV with "Date" as a normal column
        file_name = f"{symbol}_{start_date}_to_{end_date}.csv"
        file_path = os.path.join(save_dir, file_name)
        data.to_csv(file_path, index_label="Date")

        print(f"Data for {symbol} saved to {file_path}")

    except Exception as e:
        print(f"Failed to fetch data for {symbol}. Error: {e}")

# Test
if __name__ == "__main__":
    fetch_historical_data("AAPL", "2024-01-01", "2025-01-28")
