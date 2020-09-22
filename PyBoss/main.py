# PYTHON BOSS CHALLENGE

import os
import csv

# ************************** FOR GRADER **************************************************************************************
# I have an issue with setting the csv path. Basically, on my end, I have to write out the full path or the code does not run. 
# My instructor and TA have been helping me but we have not resolved this.
# For your grading, I am assuming the typical shorthand path should work:
# csvpath = os.path.join ('..', 'Resources', 'employee_data_csv')
# ****************************************************************************************************************************

csvpath = os.path.join('/Users/nicolemuscanell/UCF-03-PYTHON/PyBoss/Resources', 'employee_data.csv')

# Define new lists
emp_id = []
full_name = []
first_name = []
last_name = []
dob = []
dob_split = []
dob_new = []
ssn = []
ssn_split = []
ssn_new = []
state_new = []

# Change state names to abbreviations by creating a dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)
    
    # Add employee id to list
    for row in csv_reader:
        emp_id.append(row[0])

    # Split full name into first and last name columns and add to lists
        name = row[1] 
        full_name = name.split(" ")
        first_name.append(full_name[0])
        last_name.append(full_name[1])

    # Change date format to MM/DD/YYYY and add to list
        dob = row[2]
        dob_split = dob.split("-")
        dob_new.append(f"{dob_split[1]}/{dob_split[2]}/{dob_split[0]}")

    # Reformat SSN so that the first five numbers are hidden and add to list
        ssn = row[3]
        ssn_split = ssn.split("-")
        ssn_new.append(f"***-**-{ssn_split[2]}")

    # Reformat state from name to abbreviation and add to list
        state_abbrev = us_state_abbrev[row[4]]
        state_new.append(state_abbrev)

# Zip lists together
employees_zipped = zip(emp_id, first_name, last_name, dob_new, ssn_new, state_new)

# Specify the file path to write to
output_path = os.path.join('/Users/nicolemuscanell/UCF-03-PYTHON/PyBoss/Output', 'employee_data_new.csv')

# ************************** FOR GRADER **************************************************************************************
# output_path = os.path.join('..', 'Output', 'employee_data_new.csv')
# ****************************************************************************************************************************

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in next rows (zipped rows)
    csvwriter.writerows(employees_zipped)