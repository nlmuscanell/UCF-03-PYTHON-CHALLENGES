# PYTHON PAY CHALLENGE - ANALYSIS OF FINANCIAL INFORMATION

import os
import csv

# ************************** FOR GRADER **************************************************************************************
# I have an issue with setting the csv path. Basically, on my end, I have to write out the full path or the code does not run. 
# My instructor and TA have been helping me but we have not resolved this.
# For your grading, I am assuming the typical shorthand path should work:
# csvpath = os.path.join ('..', 'Resources', 'budget_data.csv')
# ****************************************************************************************************************************

csvpath = os.path.join ('/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyBank/Resources', 'budget_data.csv')

# ************************** FOR GRADER **************************************************************************************
# output_path = os.path.join('..', 'Resources', 'budget_data.csv')
# ****************************************************************************************************************************

# Making new lists for main analysis:
total_months = []   
total_profits = []
average_change = []

# Using csv to read the file (uses the reader object)
with open(csvpath, 'r') as csv_file:

    # Specify delimiter (comma is where data should be split) and the variable that holds the contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Skip the header row when analyzing values
    csv_header = next(csv_reader)

    # Calculate the total months & profits - add months & profits to lists created
    for row in csv_reader:
        total_months.append(row[0])
        # When printing, take the len of this list
        total_profits.append(int(row[1]))
        # When printing, ask for the sum of this list

    # Calculate the average change in profits over the entire period
    # Looping through all months in the list minus 1 to account for the index start position of zero
    for i in range(len(total_profits)-1):

    # Calculate change from month to month: the difference between one month and the one following it
    # Add these values to the average change list created earlier
        average_change.append(total_profits[i+1]-total_profits[i])

    # When printing, take this value and divide it by the total number of average change pairs compared (len of average)

# The greatest increase in profits over the entire period
    max_increase = max(average_change)

# The greatest decrease in losses over the entire period
    max_decrease = min(average_change)

# Find the date that corresponds to max and min changes in profit
# Use +1 at the end since month associated with change will be the last of the two months being compared
# On first few go arounds, saw that month returned was wrong, because it was the first of the two months being compared
    max_increase_month = average_change.index(max(average_change)) + 1
    max_decrease_month = average_change.index(min(average_change)) + 1 

# Print Analysis: Created a results variable to be able to print in a single command to the text file

Results = (
    f"Financial Analysis \n"
    f"----------------------------------------------- \n"
    f"Total Months: {len(total_months)} \n"
    f"Total profits: ${sum(total_profits)} \n"
    f"Average change in profits: ${int(sum(average_change)/len(average_change))} \n"
    f"Greatest increase in Profits: {total_months[max_increase_month]} ${max_increase} \n"
    f"Greatest decrease in profits: {total_months[max_decrease_month]} ${max_decrease} \n")

print(Results)

# ************************** FOR GRADER **************************************************************************************
# file = '..', 'Analysis', 'budget.txt')
# ****************************************************************************************************************************

# Store the file path associated with the file
file = '/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyBank/Analysis/budget.txt'

# Open the file in write mode and write results into text file
with open(file, "w") as writefile:
  
    writefile.write(Results)