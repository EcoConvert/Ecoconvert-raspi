# src/lcd_interface/config.py
import os
from dotenv import load_dotenv
from logging_config import lcd_logger  

# Load environment variables from a .env file
load_dotenv()  # Semi flag to kasi nasa global scope

# Set up logging
logger = lcd_logger(__name__)  # Create a logger for this module

def load_config():
    """
    Load application configuration from environment variables with defaults.
    Returns:
        dict: Configuration dictionary containing app settings.
    """
    logger.debug("Loading configuration...")  # Log that configuration loading has started

    config = {
        "window_title": os.getenv("WINDOW_TITLE", "RVM LCD Interface"),
        "window_width": int(os.getenv("WINDOW_WIDTH", 800)),
        "window_height": int(os.getenv("WINDOW_HEIGHT", 480)),
        "welcome_message": os.getenv("WELCOME_MESSAGE", "Let's make an Ecobrick!"),
        "instruction_text": os.getenv(
            "INSTRUCTION_TEXT", "Follow the instructions to proceed."
        ),
        "processing_status": os.getenv(
            "PROCESSING_STATUS", "Processing, please wait..."
        ),
        "completed_status": os.getenv(
            "COMPLETED_STATUS", "Operation completed successfully!"
        ),
        "qr_code_message": os.getenv(
            "QR_CODE_MESSAGE", "Scan the QR Code to complete."
        ),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
        "model_path": os.getenv("MODEL_PATH", "./resources/models/model.tflite"),
        "label_path": os.getenv("LABEL_PATH", "./resources/labels/labels.txt"),
    }

    # Log the loaded configuration (without sensitive data like paths)
    logger.debug(f"Configuration loaded: {list(config.keys())}")  # Log only the keys to avoid sensitive data leakage
    
    return config
