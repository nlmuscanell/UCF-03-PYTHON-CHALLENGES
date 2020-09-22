# PYTHON PARAGRAHP CHALLENGE - CREATE A SCRIPT AUTOMATING TEXT ANALYSIS

# HW hint said ti import regular expression operations, so my code will incorporate this
import os
import re

# ************************** FOR GRADER **************************************************************************************
# I have an issue with setting the csv path. Basically, on my end, I have to write out the full path or the code does not run. 
# My instructor and TA have been helping me but we have not resolved this.
# For your grading, I am assuming the typical shorthand path should work:
# csvpath = os.path.join ('..', 'raw_data', 'pararaph_1.txt')
# ****************************************************************************************************************************

# FIRST ANALYSIS - USING TEXT PROVIDED
file = '/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyParagraph/raw_data/paragraph_1.txt'

with open(file, 'r') as file:
  text = file.read()

# Using the split function to separate text by singles spaces and adding this to a list
# Taking the length of of this list as the word count
word_count = len(text.split(' '))

# Using the string replacement command to remove non-letters so that only letters can be counted
letter_count = re.sub('[^a-zA-Z]', '', text)

# Using the regular expression split function to separate text by punctuation marks and adding this to a list
# The re.split function allows you to specify multiple separators (delimiters)
sentences = re.split("(?<=[.!?]) +", text)

# Number of sentences
sentence_count = len(sentences)

# Dividing the number of words by the number of sentences
average_sentence_length = word_count/sentence_count

# Dividing the number of letters by number of words
average_letter_count = len(letter_count)/word_count

# Print Analysis
print("Paragraph Analysis")
print("-----------------------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {round(average_letter_count,2)}")
print(f"Average Sentence Length: {average_sentence_length}")
print("-----------------------------")

# SECOND ANALYSIS - USING TEXT I PULLED FROM A NEWS ARTICLE
file = '/Users/nicolemuscanell/UCF-03-PYTHON-CHALLENGES/PyParagraph/raw_data/paragraph_2.txt'

# ************************** FOR GRADER **************************************************************************************
# file = '..', 'raw_data', 'paragraph_2.txt')
# ****************************************************************************************************************************

with open(file, 'r') as file:
  text = file.read()

word_count = len(text.split(' '))
letter_count = re.sub('[^a-zA-Z]', '', text)
sentences = re.split("(?<=[.!?]) +", text)
sentence_count = len(sentences)
average_sentence_length = word_count/sentence_count
average_letter_count = len(letter_count)/word_count

# Print Analysis
print("Paragraph Analysis")
print("-----------------------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {round(average_letter_count,2)}")
print(f"Average Sentence Length: {average_sentence_length}")
print("-----------------------------")