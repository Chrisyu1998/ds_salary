#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:35:09 2020

@author: cyt
"""


import requests
from data_in import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()
