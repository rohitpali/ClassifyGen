from utils import load_config, setup_logger, load_input, save_output, search_details, generate_output

def validate_input(data):
    required_fields = ["input", "asset_classification", "manufacturer", "model_no"]
    for field in required_fields:
        if field not in data or not data[field]:
            raise ValueError(f"Missing required field: {field}")

def process_input(input_data, config, logger):
    validate_input(input_data)
    retries = 0
    search_result = None

    while retries <= config["max_retries"]:
        search_result = search_details(input_data["input"], logger)
        if search_result:
            break
        logger.warning(f"Attempt {retries + 1} failed. Retrying...")
        retries += 1

    if not search_result:
        logger.error("No data found after retries. Proceeding with empty values.")
        search_result = {
            "product_line": "",
            "source_url": "",
            "summary": ""
        }

    final_input = {**input_data, **search_result}
    return generate_output(final_input)

if __name__ == "__main__":
    config = load_config("config.json")
    logger = setup_logger(config["log_file"])
    logger.info("Started...")

    try:
        input_data = load_input("input.json")
        result = process_input(input_data, config, logger)
        save_output(result, "output.json")
        logger.info("Output saved to output.json successfully.")
    except Exception as e:
        logger.exception(f"Process failed: {e}")

    logger.info("Finished...\n")
