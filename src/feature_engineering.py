def compute_rolling_mean(df, window):
    df["rolling_mean"] = df["close"].rolling(window).mean()
    return df