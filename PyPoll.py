#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path. Remember that Windows uses the backslash.
file_to_load = 'Resources\election_results.csv'
#Create a filename variable to a direct or indirect path to the file.
file_to_save = 'analysis\election_analysis.txt'
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here (mod344)
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
#Print each row in the CSV file
    #for row in file_reader:
        #print(row)
        #"print(row[0]) would print the header row"
    #Print the header row with the next() method
    headers = next(file_reader)
    print(headers)



# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote