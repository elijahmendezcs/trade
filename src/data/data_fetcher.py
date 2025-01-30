import os
import yfinance as yf

def fetch_historical_data(symbol, start_date, end_date, save_dir="data/historical"):
    """
    Fetch historical stock data using yfinance and save it as a CSV file.
    :param symbol: Stock ticker symbol (e.g., 'AAPL').
    :param start_date: Start date in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :param save_dir: Directory to save the CSV file.
    """
    print(f"Fetching data for {symbol} from {start_date} to {end_date}...")

    # Ensure save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Fetch data
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if data.empty:
            print(f"No data available for {symbol} from {start_date} to {end_date}")
            return

        # Save to CSV without redundant "Date" header row
        file_name = f"{symbol}_{start_date}_to_{end_date}.csv"
        file_path = os.path.join(save_dir, file_name)
        data.to_csv(file_path)  # No index_label to avoid redundant row
        print(f"Data for {symbol} saved to {file_path}")
    except Exception as e:
        print(f"Failed to fetch data for {symbol}. Exception type: {type(e).__name__}, Error: {e}")


# Test the function
if __name__ == "__main__":
    fetch_historical_data("AAPL", "2021-01-01", "2021-12-31")
