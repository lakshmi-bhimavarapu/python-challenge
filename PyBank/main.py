# Module for reading CSV files
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
total_months = 0
sum_profit = 0

# this holds the profit/loss value of previous row in csv
previous_row_value = 0
sum_change = 0

# my_list holds the profit/loss changes from previous day
my_list = []

# my_list_date holds the dates of those profit/loss changes
my_list_date = []

with open(csvpath, encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Iterate through all rows to calculate running count of months, sum of profit/loss
    for row in csvreader:
        total_months += 1

        # sum_profit is net profit/losses over entire period
        sum_profit = sum_profit+round(float(row[1]))
        change = int(row[1])-int(previous_row_value)
        previous_row_value = row[1]

        # my_list hold the profit/loss changes and my_list_date holds the corresponding date between 2 data rows
        my_list.append(change)
        my_list_date.append(row[0])

    # calculate the greatest increase, greatest decrease and corresponding dates
    greatest_increase = max(my_list)
    greatest_decrease = min(my_list)
    greatest_increase_index = my_list.index(greatest_increase)
    greatest_increase_date = my_list_date[greatest_increase_index]
    greatest_decrease_index = my_list.index(greatest_decrease)
    greatest_decrease_date = my_list_date[greatest_decrease_index]

    # calculate the average of price change excluding the first data row in the list
    average_change = round(sum(my_list[1:])/(len(my_list)-1), 2)

    # write the analysis content to file
    file = 'analysis/myresults.txt'
    with open(file, 'w') as text:
        text.write("Financial Analysis\n")
        text.write("----------------------------\n")
        text.write("Total Months: " + str(total_months) + "\n")
        text.write("Total: $" + str(sum_profit) + "\n")
        text.write("Average Change: $" + str(average_change) + "\n")
        text.write("Greatest Increase in Profits: " + str(greatest_increase_date)
                   + " ($"+str(greatest_increase)+")\n")
        text.write("Greatest Decrease in Profits: " + str(greatest_decrease_date)
                   + " ($"+str(greatest_decrease)+")\n")

    # print the analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: " + str(total_months))
    print(f"Total: $" + str(sum_profit))
    print(f"Average Change: $" + str(average_change))
    print(f"Greatest Increase in Profits: " + str(greatest_increase_date)
          + " ($"+str(greatest_increase)+")")
    print(f"Greatest decrease in Profits: " + str(greatest_decrease_date)
          + " ($"+str(greatest_decrease)+")")
