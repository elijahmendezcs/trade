import pandas as pd

df = pd.read_csv(
    "data/historical/AAPL_2025-01-01_to_2025-01-28.csv",
    parse_dates=["Date"],
    index_col="Date"
)
print(df.head()) # Prints the first 5 rows
print(df.tail()) # Prints the last 5 rows
print(df.columns)
