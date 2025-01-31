import pandas as pd


def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Loads and CSV file (fetched by data_fetcher.py) and cleans it, and returns a pandas DataFrame ready for analysis.
    or backtesting.
    :param filepath: Path to the CSV file.
    :return: A cleaned pandas DataFrame with a DatetimeIndex.
    """

    df = pd.read_csv(filepath, parse_dates=['Date'])

    df.setIndex('Date', inplace=True)

    df.dropna(subset=['Open', 'High', 'Low', 'Close'], how='any', inplace=True)

    df.sort_index(inplace=True)

    return df