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
    print(df)
    
    
    id_name_dict = dict(zip(df.ID, df.Name))
    parent_dict = dict(zip(df.ID, df.Parent_Id))

    def find_parent(x):
        value = parent_dict.get(x, None)
        if value is None:
            return ""
        else:
            # Incase there is a id without name.
            if id_name_dict.get(value, None) is None:
                return "" + find_parent(value)
    
            return str(id_name_dict.get(value)) +", "+ find_parent(value)
        
        df['Tag'] = df.ID.apply(lambda x: find_parent(x)).str.rstrip(', ')
        
    df.to_json(f'{sheet_name}'+'/'+f'{sheet_name}.json')