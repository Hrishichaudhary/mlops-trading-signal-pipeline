# MLOps Trading Signal Pipeline

## Overview
This project implements a reproducible batch pipeline for generating trading signals using rolling mean.

## Features
- Config-driven execution
- Deterministic runs
- Logging & observability
- Dockerized deployment

## Local Run

```bash
python run.py --input data.csv --config config.yaml --output metrics.json --log-file run.log