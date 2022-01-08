# The steps that need to be taken in order to retrieve the data and manipulate it for the purpose of ballot counting
# 1. Open the file and orient yourself with the layout.
# 2. Figure out the list of unique candidates who received votes.
# 3. For each candidate, sum up the totals votes they received by vote type.
# 4. For each candidate, figure out their total vote counts by suming up the votes by vote type.
# 5. Figure out the total vote counts by suming the total votes for all candidates and confirm that this matches the total counts from the data. 
# 6. Determine the percentage of votes for each candidate and sort the percentage of votes in decending order


# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

import csv
import os

'''file_to_load = 'Resources\election_results.csv'''
file_to_load = os.path.join("Resources", "election_results.csv")

election_data = open(file_to_load, 'r')
'''election_data.close()'''

file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World, it's me computer. ")
    txt_file.write("I know you are wondering, and yes, I can think, talk, and READ MINDS!!")
    txt_file.write("\n- Love Computer\n-------------------\nComputer\nLocation: Your Desk\nNumber: I'm a computer dummy, I use fax")
    txt_file.write("Hello World, it's me computer. ")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)

    for row in file_reader:
        
        total_votes += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

'''print(f"There are a total of {total_votes:,} votes.")
print(f"The candidates are as follows: {candidate_options}")
print(candidate_votes)'''

for candidate_name in candidate_votes:
    
    votes = candidate_votes[candidate_name]
    
    percentage_vote = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: received {percentage_vote:.2f}% of the vote.")

    if (votes > winning_count) and (percentage_vote > winning_percentage):
        winning_count = votes
        winning_percentage = percentage_vote
        winning_candidate = candidate_name

winning_candidate_message = (
    f"---------------------------\n"
    f"Winner: {candidate_name}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percetnage: {winning_percentage:.2f}%\n"
    f"---------------------------\n")
print(winning_candidate_message)