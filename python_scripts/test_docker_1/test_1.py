# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:06:16 2020

@author: Telemachos Chatzitheodorou
"""

import logging
import time

LOG_LEVEL = logging.DEBUG

diagnostic = logging.getLogger('diagnostic')
diagnostic.setLevel(LOG_LEVEL)

handler = logging.StreamHandler()
handler.setLevel(LOG_LEVEL)

formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s - %(filename)s - %(message)s")
handler.setFormatter(formatter)

diagnostic.addHandler(handler)

# Test message
API = "eurostat"
user_id = 20
property_id = 1

while True:
	diagnostic.info(f"The {API} API is being called for user_id={user_id} and property={property_id}")
	diagnostic.warning("This is a warning message")
	diagnostic.error("This is an error message")
	diagnostic.critical("This is a critical message")

	a = 5
	b = 0

	try:
	  c = a / b
	except Exception as e:
	  diagnostic.exception("This is an error message with traceback")
	time.sleep(10)