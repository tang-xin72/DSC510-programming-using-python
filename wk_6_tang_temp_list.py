#DSC 510-301
#Week 6, Programming Assignment Week 6
#Author Xin Tang
#4/18/2023

#Change control log:
'''Change #1: add input validation to detect end signal and remind the invalid input,
   date of change: 4/9/2023'''
''' Change #2: add an optional method to ask user to input all temp as a string. this is as backup only.
    method #2 is not a complete code, lack of sentinel check, but I can be easily switched between method #1 and #2. '''

#Author: Xin Tang
#Change approved by: Xin Tang
#Date move to production: NA

#first will check sentinel value, then check if enter is a number. after that will append list
# the length and max/min evaluation is done at every entry.
# if user enter sentinel value, print summary. if user exit at first enter, print a statement as well.
# method #1 treat input one by one, method #2 (disabled) treat input all in one time as string, then split into list.


# main loop
def main():
    temperatures = []
    count = 0
    max_temp = 0
    min_temp = 0
    while True:
        # find what user what to do, print out result summary when user input sentinel signal.
        user_input = input("Please enter a temperature reading as number, (enter X to end) ")
        if (user_input == 'X' or user_input =='x'):
            print('\n Ending input as you commanded')
            if count == 0:
                print(' You ends with no temperature input, no MAX or MIN temperature will be calculated')
                break
            else:
                print(' You entered', count, 'temperature readings')
                #another way to find max and min directly using max(tempratures) and min(temperatures)
                print(' Maximum Temp is:', max_temp)
                #print(max(temperatures))
                print(' Minimum Temp is:', min_temp)
                #print(min(temperatures))
                break
        else:
            try:
            # convert input into numbers, find min/max along the input,
                new_input = float(user_input)
                temperatures.append(new_input)
                count =count + 1
                if new_input > max_temp:
                    max_temp = new_input
                if new_input < min_temp:
                    min_temp = new_input
                continue
            except ValueError:
            # in case the input is not a number, prompt to try again
                print("you did not enter a valid number, please try again")
                continue


if __name__ == "__main__":
     main()

#the optional method below will take user input all at one time as string, separated by comma
#temperature = []
#user_input =[float(item) for item in input("enter a series of temp reading, separated by comma: ").split(",")]
#temperature.append(user_input)
#max_temp = 0
#min_temp = 0
#for temp in temperature:
#    if temp > max_temp:
#        max_temp = temp
#    if tempe < min_temp:
#        min_temp = temp
#count = len(temperature)

