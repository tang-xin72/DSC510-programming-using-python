#DSC 510-301
#Week 10: Programming Assignment Week 10
#Author Xin Tang
#5/17/2023

#Change control log:
'''Change #1: use default science category to get joke
   date of change: 5/16/2023
   Change #2: use string function to identify first letter of user input, so 'Yes' and 'Y' both works
   date of change: 5/16/2023
   change#3: revise get_joke function to take category input. however, keep default category as science and do not take selections
             however the code can be revised if needed to ask user to select different categories.
   date of change: 5/16/2023
'''

# Author: Xin Tang
# Change approved by: Xin Tang
# Date move to production: NA



import requests
#https://api.chucknorris.io/jokes/random?category={category}

def get_joke(category):
    baseUrl = 'https://api.chucknorris.io/jokes/random?category='
    fullUrl = baseUrl + category
    ApiData = requests.get(fullUrl)
    #ApiData = requests.get('https://api.chucknorris.io/jokes/random?category=science')
    ReturnedData = ApiData.json()
    joke = ReturnedData['value']
    print('-' * 30)
    print('\n', joke, '\n')
    print('-' * 30)

def main():
    print(f'{"*":4s}{"welcome "}{"*":8}')
    while True:
        # find what user want to do, end when user input sentinel signal.
        raw_input = input("Do you want a science joke? (enter Y for yes and N for no) ")
        user_input = raw_input[0].lower()

        if user_input == 'y':
            get_joke('science')
            continue
        elif user_input == 'n':
                print('see you next time')
                break
        else:
            print(' you enter invalid choice, please enter again', '\n')
            continue

if __name__ == "__main__":
    main()