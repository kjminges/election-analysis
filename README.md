# Module 3 Assignment - Election Analysis

## Background
The purpose of this analysis was to assist the the Colorodo Board of Elections in completing an audit of their recent state election. In this audit, we were tasked with writing code that allows the Board of Elections to seemlessly summarize voter data from a text file. After receiveing a csv file with the votes, the program will calculate and display the following data:

- Total votes cast
- County data:
	- Counties where votes were cast 
	- Total number of votes per county
	- Percentage of total votes cast per county
	- Which county had the largest turnout
- Candidate data:
	- The candidates who received votes
	- Total number of votes each candidate received
	- Percentage of total votes each candidate received
	- Winner of the Election
		- Which candidate received the most votes
		- The total number of votes the winning candidate received
		- The percetnage of total votes the winning candidate received

The results of the program will give the Board of Elections data to compare against the system they currently use to tabulate results and provide them with verification of their conclusions. our hope is that this code can be used to calculate results for all future state congressional elections. 

## Election-Audit Results
The Colorodo Board of Elections has asked us to provide answers to the following questions based on our analysis of the data. Our answers can be found in the bullet underneith each numbered question:

1. How many votes were cast in this congressional election?
	- In total, there were 369,711 total votes cast in the recent congressional election.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
	- There are three counties in the congressional district: Jefferson county, Denver county, and Arapahoe county. A breakdown of the results, including percent of total votes and the raw number of votes by county, can be found in the screenshot below (note that this screen shot is a subsection of the text file that the program will generate for the Board):

**Count Election Results**
![Count Election Results](https://github.com/kjminges/Election_Analysis/blob/main/Resources/county_votes.png)

3. Which county had the largest number of votes?
	- Denver county contained the largest number of votes out of the three counties.
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
	- In this election, there were three candidates that received votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. A breakdown of the results by candidate, including votes received and the percent of total votes, can be found in the screenshot below (note that this screen shot is a subsection of the text file that the program will generate for the Board):

**Candidate Election Results**
![Candidate Election Results](https://github.com/kjminges/Election_Analysis/blob/main/Resources/candidate_votes.png)

5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
	- The winner of the congressional election was **_Diana DeGette_**. She received 272,892 votes which accounted for a total of 73.8% of the votes cast in this election. Congradulations Diana!

## Conclusion
The program that was provided to the Colorodo Board of Elections will allow the Board to reproduce the election results discussed above for any other congressional district, provided that the data received is saved under the same name and is in the same format (i.e., the first three columns contain Ballot Id, county , and candidate **in that order**) as the data used for this analysis. If the election data comes in a different format or with a different name, the code can work but it will need to be edited before it is run.

First, we need to identify the file where the election data is stored in relation to where the Python code is saved. For simplicity, it is best to save the data in the same folder as the Python code or in a sub-folder. Next, we will need to edit the code in line 9 of the code (see the second line of code below). If the data is saved in the same folder as the Python code, please remove '"Resoures," '. If the data is contained in a sub-folder, replace  the 'Resources' with the name of the folder. Make sure the name of the folder is in quotes. If the name of the data file received is different, change the "election_results.csv" to match the name of the file including the file type indicator. This should also be in quotes. 

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("sub-folder_name", "name_of_file.csv")
```

Second, identify which column contains the  names of the candidates each person voted for and the column which contains the county in which the vote came from. Then edit the number in the square brackets on line 47 of the code to match the column number of the data that contains the candidate name, but make sure to **subtract one** from the number (column numbers start from 0). Perform a similar adjustment for the number in the square brackets on line 50 for the county name. An example of the code can be found below in the fourth-to-last and last lines.

```
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```

Once these changes are made, the program will be able to run. Please reach out with any questions.  
