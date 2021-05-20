# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:40:58 2021

@author: Johann
"""

import os, csv

dir = r'C:\xampp\htdocs\charte\SVG-World-Map\returns\csv'

with open(dir + '\CH\CH2.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print (row[0])