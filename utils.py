import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)

def log_message(message):
    logging.info(message)
