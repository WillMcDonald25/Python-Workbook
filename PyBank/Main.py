import os
import csv

total_months = 0
total_profitloss= 0
change_month = []
change_profitloss= []
greatest_increase= ["", 0]
greatest_decrease= ["", 99999999999]


#define the file path
csvpath = os.path.join('Resources', 'budget_data.csv')
print("Financial Analysis")
print("----------------------------------------")
months = []
profitloss = []

#open the csv file with csv reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #create the first for loop through rows in csvfile
    for row in csvreader:
        months.append(row[0])
        profitloss.append(row[1])

        #calculate total months
        total_months = total_months + 1 
        
        #calculate total profit/loss 
        total_profitloss =  total_profitloss + int(row[1])
        previous_profitloss=0
        change_profitloss = int(row[1]) - previous_profitloss
        previous_profit = int(row[1])
        
        #find the greatest increase and decrease between months
        if (change_profitloss > greatest_increase[1]):
            greatest_increase[0]= row[0]
            greatest_increase[1]= change_profitloss
        
        if (change_profitloss < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_profitloss

   #print all equations into terminal
    print(f'total months: {total_months}')
    print(f'total profit/loss: {total_profitloss}')
    print(f'profit/loss change: {change_profitloss}')
    print(f'greatest increase: {greatest_increase[0]} {greatest_increase[1]} ')
    print(f'greatest decrease: {greatest_decrease[0]} {greatest_decrease[1]} ')

#print the output into a seperate txt file
Output= (
    f'Financial Analysis'
    f'------------------------------'
    f'total months: {total_months}'
    f'total profit/loss: {total_profitloss}'
    f'profit/loss change: {change_profitloss}'
    f'greatest increase: {greatest_increase[0]} {greatest_increase[1]} '
    f'greatest decrease: {greatest_decrease[0]} {greatest_decrease[1]} ')
    

#export the output into a txt file
with open("PyBank.txt", "w") as txt_file:
        txt_file.write(Output)

        








 

    

 




              

              
              




     

        

