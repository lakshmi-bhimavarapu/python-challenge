import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
total_count = 0
my_candidates = []
previous_unique = ''
file_output = ""

with open(csvpath, encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Iterate through all rows to calculate running count of total votes
    for row in csvreader:
        total_count += 1
        current_candidate = row[2]
        previous_unique = current_candidate
        my_candidates.append(row[2])

# using list comprehensions along with set and count functions. set() determines unique values in list.
candidate_votes = [[candidate, my_candidates.count(
    candidate)] for candidate in set(my_candidates)]

# using sort to sort the values by candidate name (ascending) to print the list
candidate_votes = sorted(candidate_votes, reverse=False)

for (candidate, votes) in candidate_votes:
    percent_votes = round((votes / total_count) * 100, 3)
    file_output = file_output + f"{candidate}: {percent_votes}% ({votes})\n"

# sort the candidate list descending to have highest votes on the top
winner_candidate = sorted(
    candidate_votes, key=lambda x: x[1], reverse=True)

print("----------------------------")

full_output = (f"Election Results\n"
               + f"----------------------------\n"
               + f"Total Votes: {total_count}\n"
               + f"----------------------------\n"
               + file_output
               + f"----------------------------\n"
               + f"Winner: {winner_candidate[0][0]}\n"
               + f"----------------------------\n"
               )
print(full_output)

election_results = os.path.join('analysis', 'myresults.txt')
with open(election_results, 'w') as myresults:
    print(full_output, file=myresults)
