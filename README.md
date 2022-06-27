# Election Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received voted.
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 

## Summary 
The analysis of the election show that: 

There were 369,711 votes cast in the election.

The candidates were:
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane

The candidate results were: 
- Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes. 
- Diana DeGette received 73.8% of the vote and 272,892 number of votes.
- Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

The winner of the election was: Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
The election commission has requested some additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each coutny out of the total count
- The county with the highest turnout

## Challenge Summary 
### Overview of Election Audit: 
The purpose of this election audit analysis was to determine the number of votes per county and which county had the highest turnout for voters in this election. This way, we can compare each county against the total number of votes collected to analyze which county produces the most voters. 

![election_results_deliverable](/election_results_deliverable.png)

### Election-Audit Results:

There were 369,711 votes cast in the election.

The counties were:
- Jefferson
- Denver
- Arapahoe

The county results were:
- Jefferson received 10.5% of the vote and 38,855 number of votes.
- Denver received 82.8% of the vote and 306,055 number of votes.
- Arapahoe received 6.7% of the vote and 24,801 number of votes.
Denver county received the highest number of votes. 

### Election-Audit Summary: 
This script can be modified to determine the relationship between turnout for counties and for counting candidate votes with any election by changing the contents of the dictionaries used here to represent which candidates were involved and which counties were involved. The script should be able to then translate into using a different set of data, as long as these definitions in the dictonary are changed. In addition, the script can be modified to change how we can view the results displayed. If there are more counties, we would see this automatically update (meaning there doesn't have to be just three counties for this script to work), and also if there are more than three candidates we could be able to display them all using this script. A different way to modify the script itself for any election would also be that if we had different sets of information to put into the election winner summary, we could add that in the section depicted below. This way there could be more statistics involved such as any other information on the voters themselves like sex, race, and age, as well as other information that could be helpful such as how many votes were counted at various poll places to see which areas in the counties are being used the most. 

![modification_1_ch3](/modification_1_ch3.png)
