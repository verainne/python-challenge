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
