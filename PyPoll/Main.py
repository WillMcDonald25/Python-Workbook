import os
import csv
import collections as ct


total_votes=0
Candidate_name= []
candidate_votes=0



#define the file path
csvpath = os.path.join('Resources', 'election_data.csv')
print('Election Results')
print('----------------------------------')
ballot_ID = []
County = []
Candidate= []

#open file with csvreader
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
        
        #Calculate candidate count
        
        votes = ct.Counter()
    
        for line in csvfile:
            candidate = line.split(",")[-1].strip()
            votes[candidate] += 1
            winner= max(votes)
        print(votes)
        print(winner)


#Export the output of the code into a txt file
output= (
    f'Election Results'
    f'------------------------'
    f'Total Votes: {total_votes} '
    f'------------------------'
    f'{votes}')

with open("PyPoll.txt", "w") as txt_file:
        txt_file.write(output)




    










    
        

        





        





