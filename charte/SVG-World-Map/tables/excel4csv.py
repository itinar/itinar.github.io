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


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile>)
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
   print ('Input file is "', inputfile)

data = pd.read_excel('countriesTest03.xlsx', sheet_name=None)

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