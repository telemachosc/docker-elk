# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:25:13 2020

@author: Telemachos Chatzitheodorou
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
print('###########---Algos init---_###################d')

from .Logger import get_logger

__all__=['get_logger']


