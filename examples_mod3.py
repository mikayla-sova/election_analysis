#F-strings: Formatted String Laterals
#Original Code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I recieved " + str(percentage_votes)+"% of the total votes.")
#F-string Code 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I recieved {my_votes / total_votes * 100}% of the total votes.")

#Using F-strngs with Dictionaries
#Code for skill drill printing each county and registered voter from the counties dictionary. 
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
#Using F-strings
for county, voters in counties_dict.itmes():
    print(f"{county} county has {voters} registered voters.")

#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the toal number of votes in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}"
    f"You recieved {candidate_votes / total_votes * 100}% of the total votes."
)
print(message_to_candidate)
#If you input 3345 for the candidate's votes and 23123 for the total votes, you get 14.466115988409808% of the total votes. 

#Format Floating-Point Decimals
#We can format numbers with a thousands separator and specify a decimal precision.
f'{value:{width}.{precision}}'
#width = number of characters used to display the value. precision = number of decimal places to format the value
message_to_candidate = (
    f"You recieved {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}"
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes."
)
#Now when we get an output, we will see the numbers with commas and the percentage as 14.47% of the total votes.


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#Copied and pasted from another example in 3.4.3
#Mod 3.4.2 Tells us how to indirectly retreive the file with chaining.
#using the open() function with the "w" mode we will write data to the file. / Use the open statement to open the file as a text file. / Changed again to using the with statement. 
with open(file_to_save, "w") as txt_file:
#Write some data to the file. / Replacing with counties. [[\n instead of a comma will produce a new line.]]
    txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")
