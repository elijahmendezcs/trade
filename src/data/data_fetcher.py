import requests
import os
import time
from datetime import datetime


def fetch_historical_data(symbol, start_date, end_date, save_dir="data/historical"):
    """
        Fetch historical stock data from Yahoo Finance and save it as a CSV file.

        :param symbol: Stock ticker symbol (e.g., 'AAPL').
        :param start_date: Start date in 'YYYY-MM-DD' format.
        :param end_date: End date in 'YYYY-MM-DD' format.
        :param save_dir: Directory to save the CSV file.
        """

    start_timestamp = int(time.mktime(datetime.strptime(start_date, "%Y-%m-%d").timetuple()))
    end_timestamp = int(time.mktime(datetime.strptime(end_date, "%Y-%m-%d").timetuple()))

    url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}"
    params = {
        "period1": start_timestamp,
        "period2": end_timestamp,
        "interval": "1d",
        "events": "history",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        os.makedirs(save_dir, exist_ok=True)

        file_path = os.path.join(save_dir, f"{symbol}.csv")
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Data for {symbol} saved to {file_path}")
    else:
        print(f"Failed to fetch data for {symbol}. Error: {response.status_code}, {response.text}")



if __name__ == "__main__":
    fetch_historical_data("AAPL", "2021-01-01", "2021-12-31")
