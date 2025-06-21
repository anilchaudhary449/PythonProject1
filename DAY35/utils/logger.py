# logger.py

import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # You can use DEBUG, WARNING, ERROR etc.

    if not logger.handlers:  # Avoid duplicate handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler('test_log.log')  # Save logs to file
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()  # Also show logs in terminal
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
