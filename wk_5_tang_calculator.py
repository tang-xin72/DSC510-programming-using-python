#DSC 510-301
#Week 5, Programming Assignment Week 5
#Author Xin Tang
#4/12/2023

#Change control log:
'''Change #1: import keyboard package to identify user input,
define function round_up to do round up so all result will be round up to certain digits
#date of change: 4/12/2023'''

#change #2: add main()


#Author: Xin Tang
#Change approved by: Xin Tang
#Date move to production: NA

import math
# import keyboard

#define function to round up numbers to user defined digits
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

#define function to calculate average
def CalculateAverage():
 number_list = []
 qty = int(input("Enter how many numbers you want to average "))

# to make code simple, the following code work on integer only, it can work on float number by change int() to float()
 for i in range(0, qty):
    print("Enter integer number at index", i, )
    item = int(input())
    number_list.append(item)
 list_sum = sum(number_list)
 list_average = list_sum / len(number_list)
 print("Average value of the numbers from input is:", round_up(list_average, 2), "\n")

#define function to calculate 2 numbers
def Calculate2Numbers():
 first_number = float(input("Enter first number: "))
 second_number = float(input("Enter second number: "))
 if second_number == 0: #remind user not try devided by zero
     print("please do not select division, can not divide by zero")

 operator = input('\n Specify the math operation here (+, -, *, /, %): ')

 if operator == '+':
  print("sum of", first_number, "and", second_number, "is:", first_number + second_number, "\n")
 elif operator == '-':
  print("substract result is", first_number - second_number, "\n")
 elif operator == '*':
  print("multiply result is", first_number * second_number, "\n")
 elif operator == '/':
  while second_number == 0: # add check to ensure not divided by zero
    print("\n need a different denominator, please input second_number again")
    second_number = float(input("Enter second number: "))
  print("division result is", round_up((first_number / second_number),2),"\n")

# main loop
def main():
 while True:
    # find what user what to do
    key_pressed = input("Select what you what to do: Q to exit, A to do average, C to do calculation for 2 numbers! \n")
    if (key_pressed =='q' or key_pressed == 'Q'):
        print('Q pressed, ending loop\n')
        break
    if (key_pressed =='a' or key_pressed == 'A'):
        print('you want to do average\n')
        CalculateAverage()
        continue
    if (key_pressed =='c' or key_pressed =='C'):
        print('you want to do 2 number calculation')
        Calculate2Numbers()
        continue

if __name__ == "__main__":
    main()