import os
import csv

total_votes=0

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
print('Election Results')
print('----------------------------------')
ballot_ID = []
County = []
Candidate = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        #append rows
        ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

        #Calculate Total Votes
        total_votes = total_votes + 1 
        
        Candidate_name = row[2]
        






    print(f'total votes: {total_votes}')