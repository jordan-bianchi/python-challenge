import os
import csv

# Path to collect data from the Resources folder
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
pybank_path = os.path.join(dir_path, 'Resources')
os.chdir(pybank_path)

count = 0
total = 0
current_revenue = 0
prior_revenue = 0
change = 0
months = []
revenue = []

#Read in csv file
with open('budget_data.csv', 'r',encoding="utf-8") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    
    #Skip header
    next(csvreader)

    for row in csvreader:
        # Calculate the total number of months 
        count = count + 1
        months.append(row[0])

        # Calculate the net amount of Profit/Losses over the period
        current_revenue = int(row[1])
        total = total + current_revenue

        # Calculate the changes in Profit/Losses
        if count > 1:
            change = current_revenue - prior_revenue
            revenue.append(change)
        prior_revenue = current_revenue
    
    # Calculate the average changes in Profit/Losses
    average_change = round((sum(revenue)/len(revenue)),2)

    # Greatest increase in profits
    greatest_increase = max(revenue)
    greatest_increase_loc = revenue.index(greatest_increase)
    greatest_increase_month = months[greatest_increase_loc]

    # Greatest decrease in losses
    greatest_decrease = min(revenue)
    greatest_decrease_loc = revenue.index(greatest_decrease)
    greatest_decrease_month = months[greatest_decrease_loc]
    
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')