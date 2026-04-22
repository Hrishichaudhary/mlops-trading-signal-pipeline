def generate_signal(df):
    df["signal"] = (df["close"] > df["rolling_mean"]).astype(int)
    return df
