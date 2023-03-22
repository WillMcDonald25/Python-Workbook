import os
import csv

total_months = 0
total_profitloss= 0
change_month = []
change_profitloss= []
greatest_increase= ["", 0]
greatest_decrease= ["", 99999999999]



csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
print("Financial Analysis")
print("----------------------------------------")
months = []
profitloss = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        #add months row
        months.append(row[0])
        #add profitloss row
        profitloss.append(row[1])

         #Calculate totals
        total_months = total_months + 1 
        
        total_profitloss =  total_profitloss + int(row[1])
        #Calculate Change
        previous_profitloss=0
        change_profitloss = int(row[1]) - previous_profitloss
        previous_profit = int(row[1])
        
        #Greatest Increase and Decrease
        if (change_profitloss > greatest_increase[1]):
            greatest_increase[0]= row[0]
            greatest_increase[1]= change_profitloss
        
        if (change_profitloss < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_profitloss

    print(f'total months: {total_months}')
    print(f'total profit/loss: {total_profitloss}')
    print(f'profit/loss change: {change_profitloss}')
    print(f'greatest increase: {greatest_increase[0]} {greatest_increase[1]} ')
    print(f'greatest decrease: {greatest_decrease[0]} {greatest_decrease[1]} ')






 

    

 




              

              
              




     

        

