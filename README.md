# 📊 MLOps Trading Signal Pipeline

## 🚀 Overview

This project implements a minimal MLOps-style batch pipeline for generating trading signals using OHLCV data.

It demonstrates:

* **Reproducibility** using config-driven execution and seed control
* **Observability** through structured logging and metrics
* **Deployment readiness** via Docker (one-command execution)

---

## ⚙️ Pipeline Workflow

1. Load configuration from `config.yaml`
2. Read OHLCV dataset (`data.csv`)
3. Compute rolling mean on `close` prices
4. Generate binary trading signal:

   * `1` if `close > rolling_mean`
   * `0` otherwise
5. Output:

   * `metrics.json` → machine-readable metrics
   * `run.log` → detailed execution logs

---

## 📁 Project Structure

```
mlops-trading-signal/
├── run.py
├── config.yaml
├── data.csv
├── requirements.txt
├── Dockerfile
├── README.md
├── metrics.json
├── run.log
└── src/
```

---

## 🖥️ Local Execution

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log
```

---

## 🐳 Docker Execution

```bash
docker build -t mlops-task .
docker run --rm mlops-task
```

---

## 📊 Example Output

```json
{
  "version": "v1",
  "rows_processed": 10000,
  "metric": "signal_rate",
  "value": 0.4989,
  "latency_ms": 59,
  "seed": 42,
  "status": "success"
}
```

---

## 🧠 Design Decisions

* First `(window - 1)` rows produce NaN rolling mean → signal defaults to `0`
* Column names are normalized (lowercase + strip) to handle real-world inconsistencies
* Numeric conversion ensures correct computations after CSV parsing
* Robust error handling ensures `metrics.json` is always generated

---

## ⚠️ Error Handling

The pipeline gracefully handles:

* Missing input file
* Invalid CSV format
* Empty dataset
* Missing required columns
* Invalid configuration

---

## 🔁 Reproducibility

* Fully config-driven (`config.yaml`)
* Deterministic outputs ensured using seed control

---

## 📦 Requirements

* Python 3.9+
* pandas
* numpy
* pyyaml

---

## ✅ Key Highlights

* No hardcoded paths (CLI-driven)
* Dockerized for reproducible deployment
* Structured logging + machine-readable metrics
* Handles real-world data inconsistencies

---

## 👨‍💻 Author

Hrishi
