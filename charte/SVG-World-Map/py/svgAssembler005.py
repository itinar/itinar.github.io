# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:40:58 2021

@author: Johann
"""

from csv import reader

import json

dir_csv = r'C:/xampp/htdocs/charte/SVG-World-Map/returns/csv/'
dir_svg_from = r'C:/xampp/htdocs/charte/SVG-World-Map/src/svg/'
dir_svg_to = r'C:/xampp/htdocs/charte/SVG-World-Map/returns/svg/'

columnLoadStates = 36
columnId = 0

# json mache u lade
c = '{}'
cL = json.loads(c)

# svg afah
svg_data = open(dir_svg_from + 'topOfFile.svg').read()


# open file in read mode
with open(dir_csv + 'CH/CH.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # skip first row
    next(csv_reader)
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
    path = dir_svg_from + country
    new_svg_data = ""
    if cL[country]:
        print(country + ' --> load big map')
        new_svg_data = open(path + '_Small.svg').read()
    else:
        print(country + ' --> load small map')
        new_svg_data = open(path + '_Small.svg').read()
    svg_data += new_svg_data

svg_data += open(dir_svg_from + 'BottomOfFile.svg').read()
    
with open (dir_svg_to + 'worldAdapt.svg', 'w') as ns:
    ns.write(svg_data)