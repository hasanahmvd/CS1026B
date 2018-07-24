# Written by Syed Ahmed (sahme339)
# 28 February 2018
# CS 1026B Assignment 2
# Purpose: determine which investing machine has a higher rate of return and invest the remaining money in it
# import Investment Machine class
from investment_machine import InvestmentMachine
# list function to read, total and average the ints within the list
def listAvg(record_list):
    # set total to 0
    total = 0
    # loop through list
    for x in record_list:
        # total up all elements
        total = x + total
    # return total/number of elements for avg
    return total/len(record_list)
# function for investing set amount
def invAmount(invMachine, mNumber, amount, reps):
    # set total to 0
    total = 0
    # loop through number of times to invest
    for x in range(reps):
        # exceute invest function while totalong returns
        total = invMachine.invest(mNumber, amount) + total
    # return the total
    return total
# function for investing set percentage
def invPercent(invMachine, mNumber, currTotal, percent, reps):
    # calculate amount using percent
    amount = percent * currTotal
    # call already written invest_amount function
    total = invAmount(invMachine, mNumber, amount, reps)
    # return total
    return total
# main method
def main():
    #list to hold profit record
    listOfProfit = []
    #loop to run 100 simulations
    for x in range (100000):
        # create investment machine
        inv = InvestmentMachine()
        #set total money to 100
        totalMoney = 100
        # call investment function for each machine and deduct invested money
        invM1 = invAmount(inv, 1, 1, 10)
        totalMoney = totalMoney - 10
        invM2 = invAmount(inv, 2, 1, 10)
        totalMoney = totalMoney - 10
        # if statement to determine the more profitable machine and invest
        # half of remaining money
        if(invM1 > invM2):
            invLast = invPercent(inv, 1, totalMoney, .5, 1)
        else:
            invLast = invPercent(inv, 2, totalMoney, .5, 1)
        totalMoney = totalMoney - 40
        # add up the returns from investment
        totalProfit = invM1 + invM2 + invLast + totalMoney
        print("${:.2f}".format(totalProfit))
        # add this round to list of records
        listOfProfit.append(totalProfit)
    # average all 100,000 rounds of investment using list avg function
    print("Average for 100,000 runs is: ${:.2f}".format(listAvg(listOfProfit)))
    # program end statement
    print ('The program is now complete and you invested your remaining money in the more profitable machine!')

# run main method
if __name__ == '__main__':
    main()
