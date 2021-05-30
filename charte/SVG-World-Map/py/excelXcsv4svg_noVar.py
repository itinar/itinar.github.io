# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:38:49 2021

@author: Johann
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:13 2021

@author: Johann
"""
import pandas as pd
import os
from csv import reader
import json
import sys, getopt

# I prefer reading excel with pd.read_excel
# passing `sheet_name=None` returns a dictionary 
# with the form {sheet_name: dataframe}
# file = input("file name:")

dir_csv = r'returns/csv/'
dir_svg_from = r'svg/'
dir_svg_to = r'returns/svg/'

columnLoadStates = 36
columnId = 0

# json mache u lade
c = '{}'
cL = json.loads(c)

# svg afah
svg_data = open(dir_svg_from + 'topOfFile.svg').read()


# Count the arguments
arguments = len(sys.argv) - 1

# Output argument-wise
position = 1
while (arguments >= position):
    print ("Parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
    
print("file name:")
print(sys.argv[1])

data = pd.read_excel(sys.argv[1] + ".xlsx", sheet_name=None)

os.makedirs('returns')
os.makedirs('returns/csv')
os.makedirs('returns/json_m')
os.makedirs('returns/json_b')

i = 2

# loop through the dictionary and save csv
for sheet_name, df in data.items():
    os.makedirs('returns/csv/'+sheet_name)
    df.to_csv('returns/csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', index = False)
    print({sheet_name})
    
    if 'StatesS' in sheet_name:
        print('nei macht')
    else:
        print('macht')
        # Read in the file
        with open('returns/csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', 'r') as file :
          filedata = file.read()
    
        # Replace the target string
        filedata = filedata.replace(',0', ',')
        
        # Write the file out again
        with open('returns/csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', 'w') as file:
          file.write(filedata)
          
        # making the json part
        with open(dir_csv + '\CH\CH2.csv', 'r') as read_obj:
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
    path = dir_svg_from + "\\" + country
    new_svg_data = ""
    if cL[country]:
        print(country + ' --> load big map')
        new_svg_data = open(path + '_Big.svg').read()
    else:
        print(country + ' --> load small map')
        new_svg_data = open(path + '_Small.svg').read()
    svg_data += new_svg_data

svg_data += open(dir_svg_from + '\BottomOfFile.svg').read()
    
with open (dir_svg_to + '\\worldAdapt.svg', 'w') as ns:
    ns.write(svg_data)