import requests
from tqdm import tqdm
from config.init_config import load_model_paths
from core.logger import Logger
import os


logger = Logger("get_model")

TOML_PATH = "config/paths.toml"
init_config = load_model_paths(TOML_PATH)


def download_model() -> None:
    """
    Download model from the internet

    Params: None
    Returns: None
    """

    model_name = init_config.name
    url = init_config.url
    model_path = init_config.path

    try:
        if not os.path.exists(model_path):
            logger.info(f"Creating directory {model_path}")
            os.makedirs(model_path)
        else:
            logger.info(f"Directory {model_path} already exists")
    except Exception as e:
        logger.error(f"Error creating directory {model_path}: {e}")
        raise Exception(f"Error creating directory {model_path}: {e}")

    try:
        with open(model_path + model_name, "r"):
            logger.info(f"Model {model_name} already exists")
            return
    except FileNotFoundError:
        logger.info(f"Model {model_name} does not exist, downloading...")
    except Exception as e:
        logger.error(f"Error checking if model {model_name} exists: {e}")
        raise Exception(f"Error checking if model {model_name} exists: {e}")

    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get("content-length", 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)
    with open(model_path + model_name, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        logger.error(f"Error downloading model {model_name}")
        raise Exception(f"Error downloading model {model_name}")
    logger.info(f"Model {model_name} downloaded successfully")
