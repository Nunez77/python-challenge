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
candidate_list = []
vote_count = []

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

        # Complete list of candidates
        if line[2] not in candidate_list:
            candidate_list.append(line[2])
            # Place a 1 when the first vote is registered.
            vote_count.append(1)  
        else:
            # When it is not the first vote, find the line and add one more vote.
            vote_count[candidate_list.index(line[2])] = 1 + vote_count[candidate_list.index(line[2])]

# Calculate percentages

# Print All
print("ELECTION RESULTS")
print("--------------------")
print("Total Votes: " + str(tot_votes))
