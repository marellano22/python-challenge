import os
import csv
csvpath = os.path.join('..','PyBank''budget_data.csv')
with open('csvpath', 'r') as csvfile:
    csvreader = csv.reader(csvfile, dilimiter=',')
    print(csvreader)
     #The total number of months included in the dataset

   
