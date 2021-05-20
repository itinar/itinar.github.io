# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:40:58 2021

@author: Johann
"""

from csv import reader

import json

dir = r'C:\xampp\htdocs\charte\SVG-World-Map\returns\csv'

columnLoadStates = 36
columnId = 0

# json mache u lade
c = '{}'
cL = json.loads(c)

# open file in read mode
with open(dir + '\CH\CH2.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        print(row[columnLoadStates])
        if row[columnId] in cL:
            if row[columnLoadStates]:
                print("should be true, loading into json")
                cL[row[columnId]] = row[columnLoadStates]
        else:
            print("unknown up to now, loading into json")
            cL[row[columnId]] = row[columnLoadStates]
            
            
for country in cL:
    if cL[country]:
        print(country + ' --> load big map')
    else:
        print(country + ' --> load small map')