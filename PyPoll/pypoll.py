# Import files
import os
import csv

# Set path for file
csv_path = os.path.join('Resources', 'election_data.csv')

# Set the output of the text file
text_path = os.path.join('analysis', 'election_output.txt')

#Open CSV as Reader
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    print(f"Header:{csv_header}")
    output.write(f"Header:{csv_header}\n")

# Set variables
votes = 0
total_votes_cast = 0
candidate_s = []
candidate_wins = {}
winning_can = ""
winning_count = 0


#Total votes cast
for row in csv_reader:
    votes +=1

# A complete list of candidates who received votes and the total number of votes won by candidate
    if row[2] not in candidate_s:
        candidate_s.append(row[2])
        numberwon [row[2]] = 0
    numberwon [row[2]]+= 1

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