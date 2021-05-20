# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:40:58 2021

@author: Johann
"""

import os

dir = r'C:\xampp\htdocs\charte\SVG-World-Map\returns\json_m'

files = os.listdir(dir)


for filename in files:
    if filename.endswith("States_m.json"):
        print(filename + " comes later")
    else:
        if os.path.exists(dir+"\\"+filename[0]+filename[1]+"_States_m.json"):
            print ("load big map for " + filename[0]+filename[1])
        else:
            print ("load small map for " + filename[0]+filename[1])