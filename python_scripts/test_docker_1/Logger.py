# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:06:16 2020

@author: Telemachos Chatzitheodorou
"""

import logging
import os
import sys

import json_log_formatter


class CustomJSONFormatter(json_log_formatter.JSONFormatter):
    """Custom json format for logging."""

    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        """Add extra fields in the JSON log."""
        extra['level'] = record.levelname
        extra['module'] = record.module
        # extra['name'] = record.name # Name of the logger
        extra['message'] = message

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra


def level_picker(level: str) -> int:
    """Pick the level of logging."""
    picker = {
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    return picker.get(level, lambda: "Invalid level for logger")


def get_logger(name: str = 'diagnostic',
               level: str = 'info',
               file_handler: bool = False) -> str:
    """Define a logger along with its configuration.

    The main purpose of this logger is to send logs to stdout for filebeat to
    process. The default configuration is to send to stdout,
    the level of the logger is set at INFO and handler at console.

    Parameters
    ----------
    name : str, optional
        The name of the logger (Defaults to 'diagnostic')

    level : str, optional
        The level of the logger (Must be one of the following 'info', 'debug',
        'warning', 'error', 'critical'. Defaults to 'info')

    file_handler : bool, optional
        If you want to also write to a file (Defaults to False)

    Returns
    -------
    logging object

    Examples
    --------
    # Import the get_logger function in the module
    from Logging import get_logger
    # Define the logger
    diagnostic = get_logger()
    # write an info message
    diagnostic.info("This is an info message")

    Notes
    -----
    When writing a try-except scope or you want to catch the traceback of a
    procedure type
    >>diagnostic.exception("message")
    for the error level and for the rest set to true the exc_info parameter
    >>diagnostic.<log_level>("message", exc_info=True)
    """
    logger = logging.getLogger(name)
    log_level = level_picker(level)
    logger.setLevel(log_level)
    # Set handler
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setLevel(log_level)
    # Set formatter for the stream handler
    log_handler.setFormatter(CustomJSONFormatter())
    # Add handler to the stream logger
    logger.addHandler(log_handler)
    if file_handler:
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..'))
        path = os.path.join(file_path, 'test_log.log')
        f_handler = logging.FileHandler(path)
        f_handler.setLevel(log_level)
        # Set formatter for the file handler
        f_handler.setFormatter(CustomJSONFormatter())
        # Add file handler to the logger
        logger.addHandler(f_handler)

    return logger


if __name__=='__main__':
    diagnostic = get_logger(name='diagnostic')
    diagnostic.debug("This will not be printed")
    diagnostic.info("This will be printed")
    diagnostic.warning("and this")
    try:
        a,b = 5, 0
        c = a/b
    except Exception as e:
        diagnostic.exception(e)

