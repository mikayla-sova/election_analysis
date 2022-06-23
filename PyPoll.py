#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path. Remember that Windows uses the backslash.
file_to_load = 'Resources\election_results.csv'
#Create a filename variable to a direct or indirect path to the file.
file_to_save = 'analysis\election_analysis.txt'
#1 Initialize a total vote counter
total_votes = 0
#Candidate Options
candidate_options = []
#Declare the empty dictionary(3.5.3)
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here (mod3.4.4)
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        #print(row[0]) would print the header row"
    #Print the header row with the next() method
    headers = next(file_reader)
    #print(headers)
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1
        #3. Print the total votes
        #print(total_votes)
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count (mod 3.5.3)
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count (mod 3.5.3) - moved outside the if because we want this to be incremental
        candidate_votes[candidate_name] += 1
#Determine the percentage of votes for each candidate by looping thorugh the counts. (mod 3.5.4)
#1. Iterate through the candidate list (mod 3.5.4)
for candidate_name in candidate_votes:
    #2. Retreive vote count of a candidate. (mod 3.5.4)
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.(mod 3.5.4)
    vote_percentage = float(votes) / float(total_votes) * 100
    #To Do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #3.5.5 CODE for determining the winning candidate
    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = 
        #vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    #4. Print the candidate name and percentage of votes.(mod 3.5.4)
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
#Print the candidate list
#print(candidate_options)
#Print the candidate vote dictionary (mod 3.5.3)
#print(candidate_votes)
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)




# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote