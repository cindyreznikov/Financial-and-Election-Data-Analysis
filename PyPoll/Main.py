import os
import csv
import operator

# identify where the files are stored

election_data_csv_path = os.path.join('Resources', 'election_data_smaller.csv')
output_path = os.path.join('Resources', 'election_results.txt')

candidate_dictionary = {}

total_voters = 0
total_candidate_votes = 0
index = 0
first_candidate = 'True'

with open(election_data_csv_path) as csvfile:
    election_data_csv = csv.reader(csvfile, delimiter=",")
    csv_header = next(election_data_csv)

    #  sort by the 3rd item which is candidate and move the 1st candidate to the previous_candidate variable
    sorted_input = sorted(election_data_csv,key=operator.itemgetter(2))
        
    for row in sorted_input:
        candidate_in = str(row[2])
        total_voters = total_voters + 1

        if first_candidate:
            previous_candidate = str(row[2])
            first_candidate = False
            
        if candidate_in != previous_candidate:
            index = index + 1
            candidate_dictionary[index] = previous_candidate
            candidate_dictionary[index] = total_candidate_votes
            previous_candidate = candidate_in 
            total_candidate_votes = 1
        else:
            total_candidate_votes = total_candidate_votes + 1

# move the last candidate to the dictionary
            
index = index + 1
candidate_dictionary[index] = previous_candidate
candidate_dictionary[index] = total_candidate_votes

print("Election Results") 
print("----------------------------")
print(f"Total Votes: {str(total_voters)}")
print("-----------------------------")

for key, value in sorted(candidate_dictionary.items(), reverse=True, key=lambda item: item[1]):
   vote_percent = value/total_voters * 100
   print(f"{str(key)} {(round(vote_percent,3))}% ({str(value)})")  

print("-----------------------------")
print(f"Winner: {str(key)}")
print("-----------------------------")

file = open(output_path, 'w') 
file.write("Election Results \n") 
file.write("----------------------------\n")
file.write(f"Total Votes: {str(total_voters)}\n")

file.write("-----------------------------\n")

#For key, value in sorted(candidate_dictionary.items(), reverse=True, key=lambda item: item[1]):

for key, value in candidate_dictionary.items():
   vote_percent = value/total_voters * 100
   file.write(f"key {(round(vote_percent,3))}% ({str(value)}) \n")  

file.write("-----------------------------\n")
file.write(f"Winner: {str(key)} \n")
file.write("-----------------------------\n")

file.close()
