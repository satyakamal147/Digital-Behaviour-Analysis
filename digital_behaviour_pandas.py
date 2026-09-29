import pandas as pd
from pathlib import Path

# DataFrame = table of data
# Series = a column of data
# Index = row labels

csv_path = Path(r"C:\Users\satya\OneDrive\Desktop\python files\digital_behaviour.csv")

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")

df = pd.read_csv(csv_path)

print("First 5 rows:")
print(df.head(5))

print("\nLast 5 rows:")
print(df.tail(5))

print("\nDataFrame info:")
print(df.info())

print("\nShape:")
print(df.shape)

print("\nInstagram_Minutes column:")
print(df["Instagram_Minutes"])

print("\nStudy_Minutes column:")
print(df["Study_Minutes"])

selected_columns = df[["Instagram_Minutes", "Study_Minutes"]]
print("\nSelected columns:")
print(selected_columns.head())

print("\nDate + selected columns:")
print(df[["Date", "Instagram_Minutes", "Study_Minutes"]].head())

print("\nInstagram total:")
print(df["Instagram_Minutes"].sum())

print("\nInstagram mean:")
print(df["Instagram_Minutes"].mean())

print("\nInstagram mean rounded to 2 decimals:")
print(round(df["Instagram_Minutes"].mean(), 2))

print("\nMaximum YouTube_Minutes:")
print(df["YouTube_Minutes"].max())

filtered_data = df[df["Instagram_Minutes"] > 100]
print("\nRows where Instagram_Minutes > 100:")
print(filtered_data.head())
