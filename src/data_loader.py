import pandas as pd
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        raise Exception("Input file not found")

    try:
        df = pd.read_csv(file_path, sep=",", engine="python")
    except Exception:
        raise Exception("Invalid CSV format")

    if df.empty:
        raise Exception("CSV file is empty")

    # Fix case where everything is in one column
    if len(df.columns) == 1:
        df = df[df.columns[0]].str.split(",", expand=True)
        df.columns = [
            "timestamp", "open", "high", "low", "close", "volume_btc", "volume_usd"
        ]

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    if "close" not in df.columns:
        raise Exception(f"Missing required column: close. Found columns: {df.columns.tolist()}")

    # 🔥 CRITICAL FIX: convert to numeric
    numeric_cols = ["open", "high", "low", "close", "volume_btc", "volume_usd"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where close is NaN after conversion
    df = df.dropna(subset=["close"])

    return df