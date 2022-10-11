import os
import csv

# path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')
reportpath = os.path.join('analysis', 'budget_resport.txt')

# defined variables
totalmonths = 0
net_total = 0
average_change = 0
greatest_in = 0
greatest_dec = 0


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths += 1

        # add total months
        net_total += int(row[1])


# # total number of months included in the dataset
#print(totalmonths)

# #def print_months(month):
# # net total amount of "profit/losses" over the entire period
# #total_months = str(date[0])
# #i + with a four loop
# #only have profit change for 85 of the months

# # changes in "profit/losses" over the entire period, including average of those changes
# #profit_loss = 
# #net_total = [total_months]
# # greatest increase in profits (date/amount) over the entire period

Output = (
    f"Financial Analysis \n"
    f"----------------------------\n"
    f"\n"
    f"Total Months: {totalmonths}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_in}\n"
    f"Greatest Decrease in Profits: {greatest_dec}\n"
    


) 
print(Output)

# save results to Resources folder
with open(reportpath, "w") as txtfile:
    txtfile.write(Output)

# #greatest decrease in profits (date/amount) over the entire period




