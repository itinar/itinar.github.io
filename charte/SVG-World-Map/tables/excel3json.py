# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:13 2021

@author: Johann
"""
import pandas as pd
import os
import csv, json

# I prefer reading excel with pd.read_excel
# passing `sheet_name=None` returns a dictionary 
# with the form {sheet_name: dataframe}
#file = input("file name:")

data = pd.read_excel('exCsvJsonTest01.xlsx', sheet_name=None)
data2 = {}

# loop through the dictionary and save csv
for sheet_name, df in data.items():
    os.makedirs(sheet_name)
    df.to_csv(f'{sheet_name}'+'/'+f'{sheet_name}.csv')

    with open(f'{sheet_name}'+'/'+f'{sheet_name}.csv') as csvfile:
        csvReader = csv.DictReader(csvfile)
        for csvRow in csvReader:
            id = csvRow['state']
            data2[id] = csvRow
            root = {}
            root[csvRow['country']] = data2
            
    with open(f'{sheet_name}'+'/'+f'{sheet_name}.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(root, indent=4))
    