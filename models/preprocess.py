import pandas as pd
import os


def clean_csv(file_path: str):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)
    # Parse dates
    df['Date'] = pd.to_datetime(df['Date'])
    # Standardize category names
    df['Category'] = df['Category'].str.title()
    # Fill missing values
    df['Amount'] = df['Amount'].fillna(0)
    return df


if __name__ == "__main__":
    file_path = "../data/sample_expenses.csv"
    df = clean_csv(file_path)

    if df is not None:
        print(df.head())
    else:
        print("Failed to load CSV.")
