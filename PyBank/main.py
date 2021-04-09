# Project Objectives:
# Create a Python script that analyzes 
# the records to calculate each of the following:
# The total number of months included in the dataset CHECK
# The net total amount of "Profit/Losses" over the entire period CHECK
# Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes 
# The greatest increase in profits (date and amount) 
# over the entire period
# The greatest decrease in losses (date and amount) 
# over the entire period

import os  # For filepaths
import csv  # For handling csv files

# Define the filepath
# Could not do it as mentioned in class for some reason.
dirname = os.path.dirname(__file__)  # Had to use this to generate a full path
csvpath = os.path.join(dirname,'Resources', 'budget_data.csv')

# Variables
tot_num_mon = 0 # Total number of months
prof_loss = 0 # Profit n Loss Summatory
prof_loss_changes = 0
inc_dec = 0 # Difference between lines, increase or decrease amounth by month
change_per_month = []
accum_changes = 0 # Adds up changes
prev_row = 0
gr_inc = 0 # Greatest increase
gr_in_mo = "" # Greatest increase month
gr_dec_mo = "" # Greatest decrease month
gr_dec = 0 # Greatest decrease

# Reading using cvs module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)  # We skip the first line.
    
    for line in csvreader:
    # 1 Count The total number of months included in the dataset
        tot_num_mon = tot_num_mon + 1
    # 2 The net total amount of "Profit/Losses" over the entire period
        prof_loss = prof_loss + int(line[1])
    # 3 Calculate the changes in "Profit/Losses" over the entire period
    #   then find the average for those changes.
        inc_dec = int(line[1]) - prev_row  # Difference between lines
        prev_row = int(line[1]) # Acquires the current value for the next loop
        accum_changes = accum_changes + inc_dec  # Adding up the changes
        change_per_month.append(inc_dec) # Create a changes list

    # The greatest increase in profits (date and amount) 
    # over the entire period
        if inc_dec > gr_inc:
            gr_inc = inc_dec
            gr_inc_mo = line[0]
    # The greatest decrease in losses (date and amount) 
    # over the entire period
        elif inc_dec < gr_dec:
            gr_dec = inc_dec
            gr_dec_mo = line[0]

    # Adjust acummulated changes by substracting the first value
    accum_changes = accum_changes - change_per_month[0]

# Print All
print("FINANCIAL ANALYSIS")
print("--------------------")
print("Total Months: " + str(tot_num_mon))
print("Total Amount: $" + str(prof_loss))
print("Average Change: $" + str(round(accum_changes/(tot_num_mon-1),2)))
print("Greatest Increase in Profits: " + gr_inc_mo + " ($ " + str(gr_inc) + ")")
print("Greatest Decrease in Profits: " + gr_dec_mo + " ($ " + str(gr_dec) + ")")

# Print to text file
txtpath = os.path.join(dirname,'Analysis', 'results.txt')
with open(txtpath, 'w',) as txtfile:
    txtfile.write("FINANCIAL ANALYSIS\n")
    txtfile.write("--------------------\n")
    txtfile.write("Total Months: " + str(tot_num_mon) + "\n")
    txtfile.write("Total Amount: $" + str(prof_loss) + "\n")
    txtfile.write("Average Change: $" + str(round(accum_changes/(tot_num_mon-1),2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " + gr_inc_mo + " ($ " + str(gr_inc) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + gr_dec_mo + " ($ " + str(gr_dec) + ")\n")