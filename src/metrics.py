import json


def compute_metrics(df, config, latency_ms):
    rows_processed = len(df)
    signal_rate = df["signal"].mean()

    return {
        "version": config["version"],
        "rows_processed": rows_processed,
        "metric": "signal_rate",
        "value": float(round(signal_rate, 4)),
        "latency_ms": latency_ms,
        "seed": config["seed"],
        "status": "success"
    }


def write_metrics(metrics, output_path):
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=4)
        