<<<<<<< HEAD
# Objectives
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# Variables
tot_votes = 0

# Define the filepath
# Could not do it as mentioned in class for some reason.
dirname = os.path.dirname(__file__)  # Had to use this to generate a full path
csvpath = os.path.join(dirname,'Resources', 'election_data.csv')

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)

    for line in csvreader:
        # 1 Count The total number of months included in the dataset
            tot_votes = tot_votes + 1
=======
# Objectives
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# Variables


# Define the filepath
# Could not do it as mentioned in class for some reason.
dirname = os.path.dirname(__file__)  # Had to use this to generate a full path
csvpath = os.path.join(dirname,'Resources', 'election_data.csv')

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)

>>>>>>> 07adfb88aed1ead951dacc416ecb8e14fde5f535
