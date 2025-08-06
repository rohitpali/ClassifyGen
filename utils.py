import logging
import time
import json

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)

def setup_logger(log_file):
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()

def load_input(path="input.json"):
    with open(path, "r") as f:
        return json.load(f)

def save_output(output, path="output.json"):
    with open(path, "w") as f:
        json.dump(output, f, indent=4)

def search_details(query, logger):
    logger.info(f"Searching for: {query}")
    time.sleep(1)
    return None  # Simulated no result

def generate_output(data):
    return {
        "asset_classification": data["asset_classification"],
        "manufacturer": data["manufacturer"],
        "model_no": data["model_no"],
        "product_line": data.get("product_line", ""),
        "source_url": data.get("source_url", ""),
        "summary": data.get("summary", "")
    }
