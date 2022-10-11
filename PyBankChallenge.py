import os
import csv

# path to collect data from the Resources folder
cvspath = os.path.join('Resources', 'budget_data.csv')

totalmonths = []

with open(cvspath) as csvfile:

    csvreader = csv.reader(csvfile)
    print(cvsreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths.append(row[0])
        #print(row[0],row[1])
        #print('\n',"-" * 75,'\n')

# total number of months included in the dataset
#def print_months(month):
# net total amount of "profit/losses" over the entire period
#total_months = str(date[0])
#i + with a four loop
#only have profit change for 85 of the months

# changes in "profit/losses" over the entire period, including average of those changes
#profit_loss = 
#net_total = [total_months]
# greatest increase in profits (date/amount) over the entire period



#greatest decrease in profits (date/amount) over the entire period




