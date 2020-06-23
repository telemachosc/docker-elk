# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:06:16 2020

@author: Telemachos Chatzitheodorou
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import time
from Logger import get_logger

diagnostic = get_logger()

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