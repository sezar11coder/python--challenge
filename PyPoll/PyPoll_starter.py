# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winner= None
max_votes=0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes=total_votes + 1

        # Get the candidate's name from the row
        candidate=row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate in candidate_votes :
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        
        else :
            candidate_votes[candidate] = 1 
            

        # Add a vote to the candidate's count




    # Print the total vote count (to terminal)
print("ELECTION RESULTS")
print("------------------------------------")
print(f"TOTAL VOTES:  {total_votes}")
print("------------------------------------")

    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner
for candidate, votes in candidate_votes.items() :

        # Get the vote count and calculate the percentage
        vote_percentage = (votes / total_votes) * 100 
        print(f"{candidate} :  {vote_percentage : .3f}%   ({votes})")

        # Update the winning candidate if this one has more votes
        if votes > max_votes :
            max_votes = votes 
            winner = candidate

        # Print and save each candidate's vote count and percentage
    


    # Generate and print the winning candidate summary
print("-------------------------------------------")
print(f"WINNER: {winner}" )  
print("-------------------------------------------")

    # Save the winning candidate summary to the text file 
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
     txt_file.write("ELECTION RESULTS\n")
     txt_file.write("----------------------------------\n")
     txt_file.write(f"TOTAL VOTES : {total_votes} \n ")
     txt_file.write("----------------------------------\n")
     for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate} : {vote_percentage:.3f}%  ({votes}) \n" )
     txt_file.write("-----------------------------------\n")
     txt_file.write(f"WINNER : {winner}\n")
     txt_file.write("----------------------------------\n")



