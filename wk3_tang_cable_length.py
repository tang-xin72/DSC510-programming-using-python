#DSC 510-301
#Week 2, Programming Assignment Week 2
#Author Xin Tang
#3/28/2023

#Change control log:
#Change #1: import math package, define function round_up to do round up so all $ value do not go beyond cents.
#date of change: 3/21/2023
#Change #2: add a while loop to check user input on cable length to ensure length is a number(integer or float but not string)
#date of change: 3/21/2023
#Change#3: add function install_cost_cal to calculate install cost with discount per length
#Author: Xin Tang
#Change approved by: Xin Tang
#Date move to production: NA



#This is a program to calculate total cost of fiber optic cables user entered


import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def install_cost_cal(length, unit_cost):
    cost = length*unit_cost
    return cost

#print welcome msg
print("\t ** Welcome to fiber optics cable store! **")
print("\t ** please enter info as prompted: **\n")

#ask customer info
Customer_name = input(" Enter you name and hit enter:\t")
print ("\t welcome", Customer_name, end = "\n")

#ask customer company name
Company_name = input(" Enter you company name and hit enter:\t")
print ("\t your company is", Company_name, end = "\n")

#ask cable length and check if it is a valid input, then pass it to variable length_val
while True:
 Cable_length = input(" Enter length of cable in ft and hit enter:\t")
 try:
   # convert it into integer
   length_val = int(Cable_length)
   print ("\t you ordered", Cable_length, "ft\n")
   break
 except ValueError:
  try:
   # if not integer, then convert it into float
   length_val = float(Cable_length)
   print ("\t you ordered", Cable_length, "ft\n")
   break
  except ValueError:
   # in case the input is not a number, prompt to try again
   print ("you did not enter a valid number, please try again")

#calculate install unit price with discount factor
if length_val <= 100:
    unit_cost = 0.87
elif length_val <=250:
    unit_cost = 0.8
elif length_val <=500:
    unit_cost = 0.7
else:
    unit_cost = 0.5

#Calculate install_cost:
Install_cost = install_cost_cal(length_val, unit_cost)

#assume cable cost is $10 per ft, calculate cable cost
Cable_cost = 10*length_val

#calculate total cost
Total_cost = Cable_cost + Install_cost

print(" *** Appreciate Your Business:", Customer_name, "from", Company_name, "***")
print("\t   You ordered\t\t", Cable_length, "ft cables")
print("\t   Material cost:\t", "$", round_up(Cable_cost,2))
print("\t   Install cost:\t", "$", round_up(Install_cost,2))
print("\t   Total cost:\t\t",  "$", round_up(Total_cost,2))
print("\t   Have A Good Day!")