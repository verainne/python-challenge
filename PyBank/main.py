import os, csv
from pathlib import Path 

# Declare file location
input_file = Path(r"C:\Users\Paige\Desktop\Class\Starter_Code\PyBank\Resources\budget_data.csv")

# Variable Lists
tm = []
profit_data = []
monthly_changes = []
 
#  CSV reader with delimiter and variable that holds contents
with open(input_file,newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels
    header = next(csvreader)  

    # Cycle through rowss
    for row in csvreader: 

        # Rows and Profit append
        tm.append(row[0])
        profit_data.append(int(row[1]))

    # Go through profits to find range
    for i in range(len(profit_data)-1):
        
        # find the differnece between monthly profits
        monthly_changes.append(profit_data[i+1]-profit_data[i])
        
# Minimum and Maximum increases
max_increase_value = max(monthly_changes)
max_decrease_value = min(monthly_changes)

increase = monthly_changes.index(max(monthly_changes)) + 1
decrease = monthly_changes.index(min(monthly_changes)) + 1 

# Check in console that the code works with print

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(tm)}")
print(f"Total: ${sum(profit_data)}")
print(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}")
print(f"Greatest Increase in Profits: {tm[increase]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {tm[decrease]} (${(str(max_decrease_value))})")

# Export to text and set the filepath 
filepath = os.path.join(r"C:\Users\Paige\Desktop\Class\Starter_Code\PyBank\Resources\PyBank_Results.txt")
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print(f"Total Months: {len(tm)}", file=text_file)
    print(f"Total: ${sum(profit_data)}", file=text_file)
    print(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}", file=text_file)
    print(f'Greatest Profit Increase: {tm[increase]} (${(str(max_increase_value))})', file=text_file)
    print(f'Greatest Profit Decrease: {tm[decrease]} (${(str(max_decrease_value))})', file=text_file)