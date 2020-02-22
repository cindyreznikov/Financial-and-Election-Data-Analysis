import os
import csv
import operator

# identify where the files are stored

election_data_csv_path = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join('..','Resources', 'election_results.txt')

candidate_dictionary {}

total_voters = 0
total_candidate_votes = 0

with open(election_data_csv_path) as csvfile:
    election_data_csv = csv.reader(csvfile, delimiter=",")
    csv_header = next(election_data_csv)

    #  sort by the 3rd item which is candidate and move the 1st candidate to the previous_candidate variable
    sorted_input = sorted(election_data_csv,key=operator.itemgetter(2))
    previous_candidate = str(row[2])

     for row in sorted_input:
         candidate_in = str(row[2])
         total_voters = total_voters + 1
                
        if candidate_in != previous_candidate:
            candidate_dictionary(candidate_in: total_candidate_votes)
            previous_candidate = candidate_in 
            total_candidate_votes = 1
        else:
            total_candidate_votes = total_candidate_votes + 1

print("Election Results") 
print("----------------------------")
print(f"Total Votes: {str(total_voters)}")
print("-----------------------------")

For key, value in sorted(candidate_dictionary.items(), key=lambda item: item[1]):
   vote_percent = value/total_voters
   print("key, + vote_percent, + ( value + ) )  

print("-----------------------------")
print(f"Winner: value[1]")
print("-----------------------------")

file = open(output_path, 'w') 
file.write("Election Results \n") 
file.write("----------------------------\n")
file.write(f"Total Votes: {str(total_voters)}\n")

print("-----------------------------")

For key, value in sorted(candidate_dictionary.items(), key=lambda item: item[1]):
   vote_percent = value/total_voters
   print("key, + vote_percent, + ( value + ) )  

file.write("-----------------------------")
file.write(f"Winner: value[1]\n")
file.write("-----------------------------")

file.close()
