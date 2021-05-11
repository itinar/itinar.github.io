# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:13 2021

@author: Johann
"""
import pandas as pd
import os

# I prefer reading excel with pd.read_excel
# passing `sheet_name=None` returns a dictionary 
# with the form {sheet_name: dataframe}
#file = input("file name:")

data = pd.read_excel('countriesTest02.xlsx', sheet_name=None)

# loop through the dictionary and save csv
for sheet_name, df in data.items():
    os.makedirs('csv/'+sheet_name)
    df.to_csv('csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', index = False)
    print({sheet_name})