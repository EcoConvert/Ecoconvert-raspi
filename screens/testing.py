import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging_config import setup_logging, lcd_logger

# Set up logging
setup_logging()

# Get a logger instance and test logging
logger = lcd_logger(__name__)

# Test logging
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
