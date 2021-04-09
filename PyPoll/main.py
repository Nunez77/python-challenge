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
candidate_qty = 0
candidate_perc = []
winner = ""

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
candidate_qty = len(candidate_list)

# Print all of the candies to the screen and their index in brackets
for i in range(len(vote_count)):
    candidate_perc.append(100*vote_count[i]/tot_votes)

# Winner candidate
max_votes = max(vote_count)
max_v_ind = vote_count.index(max_votes)
winner = candidate_list[max_v_ind]

# Print All
print("ELECTION RESULTS")
print("--------------------")
print("Total Votes: " + str(tot_votes))
print("--------------------")

# Print Results
for t in range(candidate_qty):
    print(candidate_list[t] + ": " + str(round(candidate_perc[t],3)) + "% (" + str(vote_count[t]) + ")")

# Print Winner
print("--------------------")
print("Winner: " + winner)
print("--------------------")

# Print to text file
txtpath = os.path.join(dirname,'Analysis', 'results.txt')
with open(txtpath, 'w',) as txtfile:

    txtfile.write("ELECTION RESULTS\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Votes: " + str(tot_votes) + "\n")
    txtfile.write("--------------------\n")

    # Print Results
    for t in range(candidate_qty):
        txtfile.write(candidate_list[t] + ": " + str(round(candidate_perc[t],3)) + "% (" + str(vote_count[t]) + ")\n")

    # Print Winner
    txtfile.write("--------------------\n")
    txtfile.write("Winner: " + winner + "\n")
    txtfile.write("--------------------\n")