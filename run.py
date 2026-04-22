import argparse
import time
import sys
import json

from src.config import load_config
from src.data_loader import load_data
from src.feature_engineering import compute_rolling_mean
from src.signal import generate_signal
from src.metrics import compute_metrics, write_metrics
from src.logger import setup_logger


def main(args):
    logger = setup_logger(args.log_file)

    start_time = time.time()
    logger.info("Job started")

    try:
        # Load config
        config = load_config(args.config)
        logger.info(f"Config loaded: {config}")

        # Load data
        df = load_data(args.input)
        logger.info(f"Rows loaded: {len(df)}")

        # Feature engineering
        df = compute_rolling_mean(df, config["window"])
        logger.info("Rolling mean computed")

        # Signal generation
        df = generate_signal(df)
        logger.info("Signal generated")

        # Metrics
        latency_ms = int((time.time() - start_time) * 1000)
        metrics = compute_metrics(df, config, latency_ms)

        write_metrics(metrics, args.output)
        logger.info(f"Metrics written: {metrics}")

        logger.info(f"Total latency: {latency_ms} ms")
        logger.info("Job ended with status: success")
        
        print(json.dumps(metrics))

    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)

        error_metrics = {
            "version": "v1",
            "status": "error",
            "error_message": str(e)
        }

        write_metrics(error_metrics, args.output)
        logger.error(f"Error occurred: {str(e)}")

        print(error_metrics)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--log-file", required=True)

    args = parser.parse_args()

    main(args)