# This program computes the reward of a carnival game where a toonie is tossed and reward is given if it does not lands on a line
from random import random # import random so random number can be generated later 

#Ask user for distance and reward and store as float variables
distance = float(input("Please enter the distance between lines (in mm): "))
reward = float(input("Please enter the 'reward' if the customer wins (in $): "))

#Define variables including counter
upperLimit = float(3*distance)
hits = 0

#Define constants, radius of toonie
RADIUS = 14

#Set for loop which plays 1000 times and checks if the radius of toonie is on randomly generated to fall on the lines
for i in range(999):
    on_line = False
    x = random() * upperLimit #Generates where the coin is randomly placed on x axis
    y = random() * upperLimit #Generates where the coin is randomly placed on y axis
    for k in range(3):
        if(abs((k*distance)-x) <= 14): #Checks to see if the x component of where it lands is within coins radius
            on_line = True
        elif(abs((k*distance)-y) <= 14): #Checks to see if the y component of where it lands is also within coins radius
            on_line = True
    if(not(on_line)):
        hits += 1 #Counter is increased with every coin toss

payout = 2000 - (hits * reward) #Defines the monetary outcome of the 1000 coin tosses

#Determines if the owner made or lost money with the 1000 tosses and outputs the appropriate statement
if (payout >= 0):
    print("For 1000 toonie tosses, you may get ${:.2f}".format(payout))
if (payout < 0):
    print("For 1000 toonie tosses, you may lose ${:.2f}".format(abs(payout)))
