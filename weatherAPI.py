#DSC 510-301
#Week 12, Final project for DSC510
#Author Xin Tang
#4/12/2023

#Change control log:
'''Change #1: import necesary package requests and datetime
define function round_up to do round up so all result will be round up to certain digits
#date of change: 4/12/2023'''

#change #2: add main()


#this is a program to fetch the weather info based on user input
'''Api Call: http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}'''

import requests
from datetime import datetime

# global variables
AppID = 'ec83f46dfbe12662beeee4a7ae75a168'
BaseURL = 'http://api.openweathermap.org/data/2.5/weather?q='

#CityName = ''
#CountryName = ''
# ==================

def Check_weather(City, Country):
 FullURL = BaseURL + City + ',' + Country + '&appid=' + AppID
 #debug code to validate FullURl works
 #print ('full url=[%s]' % FullURL.prettify())

 ApiData = requests.get(FullURL)
 ReturnedData = ApiData.json()
 #debug code to validate ApiData works
 #ApiData = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=ec83f46dfbe12662beeee4a7ae75a168")
 # print(ReturnedData)
# can also use ApiData.raise_for_status(), then try-except method
 if ReturnedData['cod'] == '404':
     print('invalid city or country: {}, pls check your input'.format(CityName))
 else:
  Temp = (ReturnedData['main']['temp'])-273.15
  WeatherSummary = ReturnedData['weather'][0]['description']
  print('------------------------')
  print('weather report: \n')
  print('Current weather:', WeatherSummary)
  print('Current temperature: {:.2f} degree C'.format(Temp))
  print('------------------------')



def main():
 while True:
    # find what user what to do
    key_pressed = input("Select what you what to do: Q to query the weather, E to exit \n")
    if (key_pressed == 'E' or key_pressed == 'e'):
        print('Thank you and Bye!\n')
        break
    if (key_pressed == 'q' or key_pressed == 'Q'):
        print('you want to know weather forecast\n')
        CityName = input('Enter your city name: ')
        CountryName = input('Enter your country ')
        print('\n')
        print('you are interested in', CityName.upper(), CountryName.upper())
        Now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print('Current date and time is:', Now)
        Check_weather(CityName, CountryName)


if __name__ == "__main__":
    main()

