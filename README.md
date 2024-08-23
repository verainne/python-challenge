# python-challenge

I'm not gonna lie, after a suggestion from a TA, I had ChatGPT help clean up these codes after I wrote them, then re-tested them to see if they still worked. And they did!
PyBank Code
import os
import csv
from pathlib import Path

# Declare file location
input_file = Path(r"C:\Users\Paige\Desktop\Class\Starter_Code\PyBank\Resources\budget_data.csv")

# Variable lists
months = []
profit_data = []
monthly_changes = []

# CSV reader with delimiter and variable
with open(input_file, newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    
    # Skip the header labels
    header = next(csvreader)

    # Cycle through rows
    for row in csvreader:
        # Rows and profit append
        months.append(row[0])
        profit_data.append(int(row[1]))

    # Go through profits to find range
    for i in range(len(profit_data) - 1):
        # Find the difference between monthly profits
        monthly_changes.append(profit_data[i + 1] - profit_data[i])

# Minimum and Maximum increases
max_increase_value = max(monthly_changes)
max_decrease_value = min(monthly_changes)

increase = monthly_changes.index(max(monthly_changes)) + 1
decrease = monthly_changes.index(min(monthly_changes)) + 1 

# Check in console that the code works with print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_data)}")
print(f"Average Change: ${round(sum(monthly_changes) / len(monthly_changes), 2)}")
print(f"Greatest Increase in Profits: {months[increase]} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {months[decrease]} (${max_decrease_value})")

# Export to text and set the filepath
output_file = Path(r"C:\Users\Paige\Desktop\Class\Starter_Code\PyBank\Resources\PyBank_Results.txt")
with open(output_file, "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {len(months)}", file=text_file)
    print(f"Total: ${sum(profit_data)}", file=text_file)
    print(f"Average Change: ${round(sum(monthly_changes) / len(monthly_changes), 2)}", file=text_file)
    print(f"Greatest Increase in Profits: {months[increase]} (${max_increase_value})", file=text_file)
    print(f"Greatest Decrease in Profits: {months[decrease]} (${max_decrease_value})", file=text_file)


PyPoll Code
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
