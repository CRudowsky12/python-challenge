# First we'll import the os module
# This will allow us to create file paths across operating systems

import os

# Module for reading CSV files

import csv

budget_csv = os.path.join('/Users/Chad/Desktop/CHAD/GitHub/python-challenge/PyBank/', 'budget_data.csv')

budget_csv

#csvfile = open(budget_csv, 'rb')

#csvfile

# CSV reader specifies delimiter and variable that holds contents
csvreader = csv.reader(budget_csv, delimiter=',')
for row in csvreader:
    
    storage[row[0]] = int(row[1])
    #if row[0] != 'Date': # Exclude the first row
    
    print(csvreader)
    
for row in csvreader:
    storage[row[0]] = int(row[1])
    #if row[0] != 'Profit/Losses': # Exclude the first row

def print_sum(a, b)…

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

>>> mean([1,2,3,4])
2.5
>>> mean([])
0…

highest = max(1, 2, 3)  # or max([1, 2, 3]) for lists

#Print to terminal?
#!/usr/bin/env python3
import sys
sys.stdout.write("Hello")

#Export to text file
import sys
sys.stdout = open('log.txt', 'w')
print 'Write this to file.'