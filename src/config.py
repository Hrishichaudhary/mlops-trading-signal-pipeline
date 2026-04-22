import yaml


def load_config(config_path):
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception:
        raise Exception("Invalid or unreadable config file")

    required_keys = ["seed", "window", "version"]

    for key in required_keys:
        if key not in config:
            raise Exception(f"Missing config key: {key}")

    return config