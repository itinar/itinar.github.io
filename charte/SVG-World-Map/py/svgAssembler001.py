# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:40:58 2021

@author: Johann
"""

import os

dir = r'C:\xampp\htdocs\charte\SVG-World-Map\returns\json_m'

files = os.listdir(dir)

print(files)

for filename in files:
    print(filename)
    if filename.endswith("States_m.json"): 
        print("skip for now")
        continue
    else:
        for filenameAgain in files:
            if os.path.exists(dir+"\\"+filenameAgain[0]+filenameAgain[1]+"_States_m.json"):
                print ("load big map for " + filenameAgain[0]+filenameAgain[1])
            else:
                print ("load small map for " + filenameAgain[0]+filenameAgain[1])
        continue
    
for filenameAgain in files:
            if os.path.exists(dir+"\\"+filenameAgain[0]+filenameAgain[1]+"_States_m.json"):
                print ("load big map for " + filenameAgain[0]+filenameAgain[1])
            else:
                print ("load small map for " + filenameAgain[0]+filenameAgain[1])