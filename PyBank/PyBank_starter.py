# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_net = None
net_changes = []
dates = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Extract date and profit/loss
        date = row[0]
        net = int(row[1])
    
        # Track the total number of months
        total_months = total_months + 1
        
        # Track the total net amount of "Profit/Losses"
        total_net = total_net + net
        
    
        dates.append(date)
    
        # Calculate changes in "Profit/Losses" from the previous month
        if previous_net is not None:
            net_change = net - previous_net
            net_changes.append(net_change)
            
            
            
        # Update the previous_net to the current month for next iteration
        previous_net = net
        

# Calculate the average net change across the entire period
average_change = sum(net_changes) / len(net_changes)

# Find the greatest increase and decrease in profits (month and amount)
greatest_increase = max(net_changes)
greatest_decrease = min(net_changes)

# Find the corresponding dates for greatest increase and decrease
greatest_increase_date = dates[net_changes.index(greatest_increase) + 1]
greatest_decrease_date = dates[net_changes.index(greatest_decrease) + 1]

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the output
print(output)


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
