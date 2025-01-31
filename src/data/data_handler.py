import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Loads a CSV file (fetched by data_fetcher.py), cleans it, and returns a pandas DataFrame ready for analysis.
    :param filepath: Path to the CSV file.
    :return: A cleaned pandas DataFrame with a DatetimeIndex.
    """

    # Load the CSV file and parse the "Date" column as datetime
    df = pd.read_csv(filepath, parse_dates=['Date'])

    # Set the "Date" column as the DataFrame index
    df.set_index('Date', inplace=True)

    # Adjust column names if they contain a suffix like "_AAPL"
    rename_columns = {
        'Open_AAPL': 'Open',
        'High_AAPL': 'High',
        'Low_AAPL': 'Low',
        'Close_AAPL': 'Close'
    }
    df.rename(columns=rename_columns, inplace=True)

    # Drop rows with missing data in these columns
    df.dropna(subset=['Open', 'High', 'Low', 'Close'], how='any', inplace=True)

    # Sort the DataFrame by its index (Date)
    df.sort_index(inplace=True)

    return df
