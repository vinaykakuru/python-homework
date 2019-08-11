# -*- coding: utf-8 -*-
"""
Week 2 Homework: PyBank

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, and iterate over each
row of the file to analyze profit trends for a bank.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path("./Resources/budget_data.csv")

# Initialize lists
months = []
profits = []

# Open the csv file as an object
with open(csvpath, "r") as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
    # Read months and profits as seperate lists    
        months.append(row[0])
        profits.append(float(row[1]))

# Initialize variables for analysis        
counter = 1
greatest_inc_index = 1
greatest_dec_index  = 1
greatest_increase = 0.0
greatest_decrease = 0.0
change_in_profit = 0.0
total_change_in_profits = 0.0

# Iterate on profits list starting at index 1 to calculate change from previous month
# Perform a check to verify the greatest increase and decrease and record the respective index
while counter < (len(profits)):
    
    # Calculate change in profit from current month to previous month
    change_in_profit = (profits[counter] - profits[counter - 1])
    # Calculate cumulative change in profit for each of the months
    total_change_in_profits += change_in_profit
    
    if  change_in_profit > greatest_increase:
        greatest_increase = change_in_profit
        greatest_inc_index = counter
    elif change_in_profit < greatest_decrease:
        greatest_decrease = change_in_profit
        greatest_dec_index = counter
    
    # Increment counter to get next element in the list
    counter +=1

# Set output file name
output_path = 'output.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write analysis to the output file
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {counter}\n")
    file.write(f"Total: ${int(sum(profits))}\n")
    file.write(f"Average Change: ${round(total_change_in_profits/(counter - 1),2)}\n")
    file.write(f"Greatest Increase in Profits: {months[greatest_inc_index]} (${round(greatest_increase)})\n")
    file.write(f"Greatest Decrease in Profits: {months[greatest_dec_index]} (${round(greatest_decrease)})\n")
