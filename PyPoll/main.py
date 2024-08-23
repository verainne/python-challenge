import os, csv
from pathlib import Path 

input_file = Path(r"C:\Users\Paige\Desktop\Class\Starter_Code\PyPoll\Resources\election_data.csv")

# Variables list
total_votes = 0
candidates = {}
winner = ""
max_votes = 0


#  CSV reader
with open(input_file) as blection:
    csvreader = csv.reader(blection,delimiter=",") 

    # Go through CSV rows
    for row in csvreader:
        total_votes += 1 
        candidate = row[2] 

        # Votes Cast
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1  

# Print the total number of votes
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
# Calculate vote percentages and determine the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print("----------------------------")
# Print the winner
print(f"The Winner Is: {winner}")

output_file_path = r"C:\Users\Paige\Desktop\Class\Starter_Code\PyPoll\Election_Results.txt"
with open(output_file_path, "w") as text_file:
    print("Election Results", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("----------------------------", file=text_file)
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})", file=text_file)
    print("----------------------------", file=text_file)
    print(f"The Winner Is: {winner}", file=text_file)