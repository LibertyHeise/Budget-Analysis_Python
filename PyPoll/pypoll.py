# Import files
import os
import csv

# Set path for file
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Set the output of the text file
text_path = os.path.join('analysis', 'election_output.txt')

# Set variables
# Total votes counter
totalvotes = 0

# Candidate Options and Vote Counters
candidate_opt = []
candidate_votes = {}

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Format for outputs

Output = (
    f"Election Results \n"
    f"----------------------------\n"
    f"\n"
    f"Total Votes: {totalvotes}\n"
    f"----------------------------\n"
    f"\n"    



    f"----------------------------\n"
    f"\n"
    f"Winner: {popularvote}")
f"----------------------------\n"



print(Output)

# save results to analysis folder
with open(text_path, "w") as txtfile:
    txtfile.write(Output)