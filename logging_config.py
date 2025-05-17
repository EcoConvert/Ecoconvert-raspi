# #!/usr/bin/env python
# import os 
# import logging 
# from logging.config import dictConfig

# os.makedirs('logs', exist_ok=True)

# config = {
# 	'version': 1,
# 	'disable_existing_loggers': False, 
# 	'formatters': {
# 		'standard': {
# 			'format': '%(asctime)s ~ %(levelname)s ~ %(message)s',
# 		}, 
# 		'coffee_formatter' : {
# 			'format' : '%(name)s : %(pathname)s : %(levelname)s : %(message)s',
# 		}
# 	},
# 	'handlers': {
# 		'default': {
# 			'level': 'DEBUG',
# 			'formatter': 'standard',
# 			'class': 'logging.StreamHandler',
# 			'stream': 'ext://sys.stdout'}, 
#         'file': {
#             'level': 'DEBUG',
#             'formatter': 'standard',
#             'class': 'logging.FileHandler',
#             'filename': 'logs/standard.log',
#             'mode': 'a'},
# 		'coffee_console': {
# 			'level': 'WARNING',
# 			'formatter': 'coffee_formatter',
# 			'class': 'logging.StreamHandler',
#             'stream': 'ext://sys.stdout'}, 
#         'coffee_file': {
# 			'level': 'DEBUG',
# 			'formatter': 'coffee_formatter',
# 			'class': 'logging.FileHandler',
#             'filename': 'logs/coffee.log',
# 			'mode':'w',}
# 	},
# 	'loggers': {
# 		"" : {
#             'level': 'INFO',
#             'handlers': ['default', 'file'],  
#             'propagate': False, },
# 		"a" : {
# 			'level' : 'DEBUG',
# 			'handlers': ['coffee_file', 'coffee_console'],
# 			'propagate': False, },
#         }, 
# }

# def setup_logging():
# 	"""Choose your handler once setup logging ran, 
# 	we can get different loggers depending on the
# 	running process. default is on logging
# 	this code: 
# 		logging.info("Bottle Valid") # will use default logger
	
# 	this code: 
# 	another_loger = logging.getLogger(__name__) # for dynamic logging
# 	if the file is in path a/b/c/module21.py
# 	then the __name__ is a.b.c.module21
# 	if "a.b.c.module21" does not exist in config.loggers it will check
# 	for "a.b.c" if none  "a.b" then "a" then if none "" 
	
# 	"""
# 	dictConfig(config)

# if __name__ == '__main__':
#     setup_logging()


# src/lcd_interface/utils/logger.py
import logging
import os


def setup_logging(log_dir="logs", log_level="INFO"):
    """
    Set up logging configuration for the application.

    Args:
        log_dir (str): Directory where log files will be stored.
        log_level (str): Logging level (e.g., "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL").

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Log file paths
    app_log_file = os.path.join(log_dir, "app.log")
    error_log_file = os.path.join(log_dir, "error.log")

    # Create the main logger
    logger = logging.getLogger("RVMInterface")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    # Log formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Application log file handler
    app_file_handler = logging.FileHandler(app_log_file)
    app_file_handler.setLevel(logging.INFO)
    app_file_handler.setFormatter(formatter)
    logger.addHandler(app_file_handler)

    # Error log file handler
    error_file_handler = logging.FileHandler(error_log_file)
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    logger.addHandler(error_file_handler)

    return logger


def lcd_logger(name):
    """
    Get a child logger with the specified name.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Child logger instance.
    """
    return logging.getLogger("RVMInterface").getChild(name)
