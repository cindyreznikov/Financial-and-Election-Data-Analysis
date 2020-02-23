import os
import csv

budget_data_csv_path = os.path.join('..', 'PyBank', 'budget_data.csv')
output_path = os.path.join('..','PyBank', 'financial_analysis.txt')

with open(budget_data_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    total_months = 0
    net_total_amount = 0
    greatest_increase = 0
    greatest_decrease = 0
    previous_month_profit_loss = 0
    monthly_difference = 0
    

    for row in csv_reader:
        month_year = str(row[0])
        profit_loss = int(row[1])
        
        total_months = total_months + 1
        net_total_amount = net_total_amount + profit_loss
        if profit_loss > 0:
             if greatest_increase < profit_loss:
                   greatest_increase = profit_loss
                   greatest_increase_month = month_year
        elif greatest_decrease > profit_loss:
                   greatest_decrease = profit_loss
                   greatest_decrease_month = month_year

avg_change = net_total_amount/total_months

print("Financial Analysis") 
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total_amount)}")
print(f"Average Change: $ {(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {str(greatest_increase_month)}  (${str(greatest_increase)})")      
print(f"Greatest Decrease in Profits: {str(greatest_decrease_month)}  (${str(greatest_decrease)})")

file = open(output_path, 'w') 
file.write("Financial Analysis \n") 
file.write("----------------------------\n")
file.write(f"Total Months: {str(total_months)}\n")
file.write(f"Total: ${str(net_total_amount)}\n")
file.write(f"Average Change: $ {(round(avg_change,2))} \n")
file.write(f"Greatest Increase in Profits: {str(greatest_increase_month)} (${str(greatest_increase)})\n")      
file.write(f"Greatest Decrease in Profits: {str(greatest_decrease_month)} (${str(greatest_decrease)})\n")
file.close()
