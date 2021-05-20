# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:46:13 2021

@author: Johann
"""
import pandas as pd
import os
import sys, getopt

# I prefer reading excel with pd.read_excel
# passing `sheet_name=None` returns a dictionary 
# with the form {sheet_name: dataframe}
#file = input("file name:")


# Count the arguments
arguments = len(sys.argv) - 1

# Output argument-wise
position = 1
while (arguments >= position):
    print ("Parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
    
print("file name:")
print(sys.argv[1])

data = pd.read_excel('countries11_sampleTest.xlsx', sheet_name=None)

os.makedirs('csv')

i = 2

# loop through the dictionary and save csv
for sheet_name, df in data.items():
    os.makedirs('csv/'+sheet_name)
    df.to_csv('csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', index = False)
    print({sheet_name})
    
    if 'States' in sheet_name:
        print('nei macht')
    else:
        print('macht')
        # Read in the file
        with open('csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', 'r') as file :
          filedata = file.read()
    
        # Replace the target string
        filedata = filedata.replace(',0', ',')
        
        # Write the file out again
        with open('csv/'+f'{sheet_name}'+'/'+f'{sheet_name}.csv', 'w') as file:
          file.write(filedata)