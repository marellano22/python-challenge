import os
import csv

# path = "/Python-challange"

# print(os.path.join(path, "PyBank"."Resources",))

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

csvpath = os.path.join(THIS_FOLDER, 'budget_data.csv')

# Reading using CSV module
with open(csvpath, "r") as csvfile:

    num_months = 0
    net_total = 0
    avg_change = 0
    greatest_increase = 0
    greatest_decrease = 0

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

 # The total number of months included in the dataset
        num_months += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total += float(row[2])

        # The average of the changes in "Profit/Losses" over the entire period
        avg_change = sum("Profit/Losses") / len("Profit/Losses")

        # The greatest increase in profits (date and amount) over the entire period
        greatest_increase = max("Profit/Losses")

        # The greatest decrease in losses (date and amount) over the entire period
        greatest_decrease = min("Profit/Losses")

        # Print answeres to terminal
        print('The total number of months is {}'.format(num_months))
        print('The total is {}'.format(net_total))
        print("The average of the changes in Profit/Losses"), avg_change)
        print("The greatest increase in Profit/Losses"), greatest_increase)
        print("The greatest decrease in Profit/Losses"), greatest_decrease)

       