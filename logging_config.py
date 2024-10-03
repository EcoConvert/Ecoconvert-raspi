#!/usr/bin/env python
import os 
import logging 
from logging.config import dictConfig

os.makedirs('logs', exist_ok=True)

config = {
	'version': 1,
	'disable_existing_loggers': False, 
	'formatters': {
		'standard': {
			'format': '%(asctime)s ~ %(levelname)s ~ %(message)s',
		}, 
		'coffee_formatter' : {
			'format' : '%(name)s : %(pathname)s : %(levelname)s : %(message)s',
		}
	},
	'handlers': {
		'default': {
			'level': 'DEBUG',
			'formatter': 'standard',
			'class': 'logging.StreamHandler',
			'stream': 'ext://sys.stdout'}, 
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'logs/standard.log',
            'mode': 'a'},
		'coffee_console': {
			'level': 'WARNING',
			'formatter': 'coffee_formatter',
			'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'}, 
        'coffee_file': {
			'level': 'DEBUG',
			'formatter': 'coffee_formatter',
			'class': 'logging.FileHandler',
            'filename': 'logs/coffee.log',
			'mode':'w',}
	},
	'loggers': {
		"" : {
            'level': 'DEBUG',
            'handlers': ['default', 'file'],  
            'propagate': False, },
		"a" : {
			'level' : 'DEBUG',
			'handlers': ['coffee_file', 'coffee_console'],
			'propagate': False, },
        }, 
}

def setup_logging():
	"""Choose your handler once setup logging ran, 
	we can get different loggers depending on the
	running process. default is on logging
	this code: 
		logging.info("Bottle Valid") # will use default logger
	
	this code: 
	another_loger = logging.getLogger(__name__) # for dynamic logging
	if the file is in path a/b/c/module21.py
	then the __name__ is a.b.c.module21
	if "a.b.c.module21" does not exist in config.loggers it will check
	for "a.b.c" if none  "a.b" then "a" then if none "" 
	
	"""
	dictConfig(config)

if __name__ == '__main__':
    setup_logging()
