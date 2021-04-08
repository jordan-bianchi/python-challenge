import os
import csv

# Path to collect data from the Resources folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
pypoll_path = os.path.join(dir_path, 'Resources')
os.chdir(pypoll_path)

votes_cast = 0
votes = []
candidate = 0
candidate_list = []
candidate_names = []
candidate_votes = []
vote_percent = []

#Read in csv file
with open('election_data.csv', 'r',encoding="utf-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    #Skip header
    next(csvreader)

    for row in csvreader:
        # Calculate the total number of votes 
        votes_cast = votes_cast + 1
        votes.append(row[0])

        # Create a complete list of candidates who received votes
        candidate = row[2]
        candidate_list.append(candidate)

    
    for x in set(candidate_list):
        candidate_names.append(x)
        # Calculate the total number of votes each candidate won
        y = candidate_list.count(x)
        candidate_votes.append(y)
        # Calculate the percentage of votes each candidate won
        z = round((y/votes_cast)*100,5)
        vote_percent.append(z)
    
    winning_votes = max(candidate_votes)    
    winner = candidate_names[candidate_votes.index(winning_votes)]
        


        
    





    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {votes_cast}')
    print("-------------------------")
    for x in range(len(candidate_names)):
        print(f'{candidate_names[x]}: {vote_percent[x]}% ({candidate_votes[x]})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
