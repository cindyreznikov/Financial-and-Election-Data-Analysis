import os
import csv

budget_data_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')
output_path = os.path.join('..','PyBank', 'financial_analysis.txt')

with open(budget_data_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    date_list = []
    profit_loss_list = []
    profit_loss_change_list = []

# load the input data into 2 lists - 1 for profit/loss, 1 for date

    for row in csv_reader:
        profit_loss_list.append(float(row[1]))
        date_list.append(row[0])

total_profit_loss = sum(profit_loss_list)
# Load the profit_loss_change list with differences between 2 dates

for i in range(1,len(profit_loss_list)):
    profit_loss_change_list.append(profit_loss_list[i] - profit_loss_list[i-1])
    avg_profit_loss_change = sum(profit_loss_change_list)/len(profit_loss_change_list) 

    min_profit_loss_change = min(profit_loss_change_list)
    max_profit_loss_change = max(profit_loss_change_list)

    max_profit_loss_change_date = str(date_list[profit_loss_change_list.index(max(profit_loss_change_list))+1])
    min_profit_loss_change_date = str(date_list[profit_loss_change_list.index(min(profit_loss_change_list))+1])


# print to the screen

print("Financial Analysis") 
print("----------------------------")
print("Total Months: ", len(date_list))
print(f"Total: ${int(total_profit_loss)}")

print("Average Change: $", (round(avg_profit_loss_change,2)))

print(f"Greatest Increase in Profits: {str(max_profit_loss_change_date)}  (${int(max_profit_loss_change)})")      
print(f"Greatest Decrease in Profits: {str(min_profit_loss_change_date)}  (${int(min_profit_loss_change)})")

# write to a csv file

file = open(output_path, 'w') 
file.write("Financial Analysis \n") 
file.write("----------------------------\n")
file.write(f"Total Months: {str(len(date_list))}\n")
file.write(f"Total: ${int(total_profit_loss)}\n")

file.write(f"Average Change: $ {(round(avg_profit_loss_change,2))} \n")
file.write(f"Greatest Increase in Profits: {str(max_profit_loss_change_date)} (${int(max_profit_loss_change)})\n")      
file.write(f"Greatest Decrease in Profits: {str(min_profit_loss_change_date)} (${int(min_profit_loss_change)})\n")
file.close()
