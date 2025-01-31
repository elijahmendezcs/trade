import pandas as pd

def load_and_clean_data(filepath):
    """Load and preprocess market data."""
    df = pd.read_csv(filepath)

    # Convert to datetime index
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
    elif 'Datetime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['Datetime'])
        df.set_index('Datetime', inplace=True)

    # Rename columns to standard names
    rename_columns = {
        'Open_AAPL': 'Open',
        'High_AAPL': 'High',
        'Low_AAPL': 'Low',
        'Close_AAPL': 'Close',
        'Volume_AAPL': 'Volume'
    }
    df.rename(columns=rename_columns, inplace=True)

    # Clean missing values
    df = df.dropna()
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # Standardize columns

    return df.sort_index()
