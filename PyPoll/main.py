# PYTHON POLL CHALLENGE - VOTE COUNTING

import os
import csv

# ************************** FOR GRADER **************************************************************************************
# I have an issue with setting the csv path. Basically, on my end, I have to write out the full path or the code does not run. 
# My instructor and TA have been helping me but we have not resolved this.
# For your grading, I am assuming the typical shorthand path should work:
# csvpath = os.path.join ('..', 'Resources', 'election_data.csv')
# ****************************************************************************************************************************

csvpath = os.path.join ('/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyPoll/Resources', 'election_data.csv')

# Making new list where candidate names will be added 
candidates = []

with open(csvpath, 'r') as csv_file:

  csv_reader = csv.reader(csv_file, delimiter=',')
  csv_header = next(csv_reader)

  # Adding candidate names to list created and using final count of names as the total vote count
  for row in csv_reader:
    candidates.append(row[2])
    total_votes = len(candidates)

  # A complete list of candidates who received votes - used set()function to see how many unique names there are
  unique_names = set(candidates)     
  print("------------------------------------")     
  print("Candidates who received votes")
  print(f"{unique_names}")
  print("------------------------------------")

  # There were four unique names in the set, so next step is to set up counters for the four candidates
  Khan = 0
  Correy = 0
  Li = 0
  OTooley = 0

  # The total number of votes each candidate won (count the number of times each candidate name occurs)
  for i in candidates:
    if i == 'Khan':
      Khan = Khan + 1
    elif i == 'Correy':
      Correy = Correy + 1
    elif i == 'Li':
      Li = Li + 1
    elif i == "O'Tooley":
      OTooley = OTooley + 1
   
  # The percentage of votes each candidate won (candidate votes divided by total votes * 100)
    Khan_percent = Khan/total_votes*100
    Correy_percent = Correy/total_votes*100
    Li_percent = Li/total_votes*100
    OTooley_percent = OTooley/total_votes*100     

    vote_percentages = [Khan_percent, Correy_percent, Li_percent, OTooley_percent]

  # The winner of the election based on popular vote 
  # Created a variable that uses the index function and identifies the candidate with the max votes
    winner_index = vote_percentages.index(max(vote_percentages))
    winner = candidates[winner_index]

# Print Analysis - created a results variable to be able to print in a single command to the text file

Results = (
  f"Election Results \n"
  f"------------------------------------ \n"
  f"Total number of votes: {total_votes} \n"
  f"------------------------------------ \n"
  f"Khan: {round(Khan_percent, 2)}% ({Khan}) \n"
  f"Correy: {round(Correy_percent, 2)}% ({Correy}) \n"
  f"Li: {round(Li_percent, 2)}% ({Li}) \n"
  f"OTooley: {round(OTooley_percent, 2)}% ({OTooley}) \n"
  f"------------------------------------ \n"
  f"The winner is {winner}! \n")

print(Results)

# Store the file path associated with the file
file = '/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyPoll/Analysis/votes.txt'

# ************************** FOR GRADER **************************************************************************************
# file = ('..', 'Analysis', 'votest.txt')
# ****************************************************************************************************************************

# Open the file in write mode and write results into text file
with open(file, "w") as writefile:
  
    writefile.write(Results)
