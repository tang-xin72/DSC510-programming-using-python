#DSC 510-301
#Week 12 assignment project for DSC510
#Author Xin Tang
#6/1/2023

#Change control log:
'''
Change #1: create 2 function to handle zip and city separately
date of change: 5/20/2023
change #2: rewrite function to handle zip and city in one function
date of change: 5/29/2023
change #3: add many error checks as possible
date of change: 5/30/23
'''



#this is a program to fetch the weather info based on user input
'''
2 different API calls used. first to get geo value based on city name or zip code, second is to fetch weather data based on Geo value.
4 functions defined
CallOpenWeatherAPI checks if webservice connection is successful. return error info if web service is failed.
PrettyPrint handles print out in a readable format
check_weather does actual check, first get Latitude and longitude value, based on if zip code or city name was selected, the methods are different.
testcase is used to simulate invalid entry 
'''
import requests
from datetime import datetime

# global variables
AppID = 'ec83f46dfbe12662beeee4a7ae75a168'
BaseGeoURL = 'http://api.openweathermap.org/geo/1.0/direct?q='
BaseURL = 'http://api.openweathermap.org/data/2.5/weather?q='
BaseUrl_by_zip = 'https://api.openweathermap.org/data/2.5/weather?zip='
UrlGeoCheck = 'https://api.openweathermap.org/data/2.5/weather?lat='

response = None
# ==================

def CallOpenWeatherAPI(url):
    global response
    
    return_flag = False #return_flag is the flag for successful web service
    try:
        response = requests.get(url)
        response.raise_for_status()
        #print("http connection [%s] was successful.")
        return_flag = True
    except requests.ConnectionError as err:
        print('http connection error happened [%s]' % str(err))
    except requests.RequestException as err:
        print('There was an undefined exception that occurred while handling your request. \n [%s]' % str(err))
    except requests.HTTPError as err:
        print('An HTTP error occurred.[%s]' % str(err))
    except requests.URLRequired as err:
        print('A valid URL is required to make a request.[%s]' % str(err))
    except requests.TooManyRedirects as err:
        print('Too many redirects.[%s]' % str(err))
    except requests.ConnectTimeout as err:
        print('The request timed out while trying to connect to the remote server.[%s]' % str(err))
    except requests.ReadTimeout as err:
        print('The server did not send any data in the allotted amount of time.[%s]' % str(err))
    except requests.Timeout as err:
        print('The request timed out.[%s]' % str(err))
    except requests.JSONDecodeError as err:
        print('Couldn’t decode the text into json [%s]' % str(err))

    return(return_flag)

def PrettyPrint():
    global response
    
    resData = response.json()
    # print(resData)
    
    Humidity = resData['main']['humidity']
    Temp = (resData['main']['temp'])-273.15
    WindSpeed = resData['wind']['speed']
    WeatherSummary = resData['weather'][0]['description']
    print('------------------------')

    print('Weather report: \n')
    print('Current weather:', WeatherSummary)
    print('Current temperature: {:.2f} degree C'.format(Temp))
    print('Current Humidity:', Humidity)
    print('Current Wind Speed:', WindSpeed)
    print('------------------------','\n')
    
def check_weather(cityName, stateName, countryName, zipCode):
    ret = False
    lat = ''
    lon = ''
    # firstly get the lat and lon
    if zipCode == '': # check weather by city/country
        fullURL = BaseGeoURL + cityName + ',' + stateName + ',' + countryName + '&appid=' + AppID
        return_flag = CallOpenWeatherAPI(fullURL)
        if (return_flag):
            # read lat and lon
            resData = response.json()
            if (len(resData) > 0) and ('lat' in resData[0]) and ('lon' in resData[0]):
                lat = str(resData[0]['lat'])
                lon = str(resData[0]['lon'])
            
    else: # check weather by zip code
        fullURL = BaseUrl_by_zip + zipCode + ',' + countryName + '&appid=' + AppID
        return_flag = CallOpenWeatherAPI(fullURL)
        if (return_flag):
            # read latitude and lontitude
            resData = response.json()
            if (len(resData) > 0) and ('coord' in resData) and \
                ('lat' in resData['coord']) and ('lon' in resData['coord']):
            
                lat = str(resData['coord']['lat'])
                lon = str(resData['coord']['lon'])
        
    if (lon == '' or lat == ''):
        print('No weather information is found, Please check your input again.')
        return
    
    newUrl = UrlGeoCheck + lat + '&lon=' + lon + '&appid=' + AppID
    #print('new url:', newUrl)
    return_flag = CallOpenWeatherAPI(newUrl)
    if return_flag:
        PrettyPrint()
    else:
        print('No weather information is found. Please check your input again.')

def main():
  print('--welcome--\n')
  while True:
    # find what user what to do
    key_pressed = input('\n Select what you what to do: Q to query the weather by city name, z to query by zip code, E to exit \n')
    short_key =key_pressed[0]
    if (key_pressed == 'E' or key_pressed == 'e'):
        print('Thank you and Bye!\n')
        break
    elif (key_pressed == 'q' or key_pressed == 'Q'):
        print('you want to know weather forecast by city name\n')
        cityName = input('Enter your city name: ')
        RawstateName = input('Enter your State name: ')
        stateName = RawstateName[0:2].lower()
        RawcountryName = input('Enter your country: ')
        countryName = RawcountryName[0:2].lower()
        print('\n')
        print('you are interested in', cityName.upper(), stateName.upper(), countryName.upper())
        Now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print('Current date and time is:', Now)
        
        check_weather(cityName, stateName, countryName, zipCode='')
        continue
    elif (key_pressed == 'Z' or key_pressed == 'z'):
            print('you want to know weather forecast by zip code\n')
            zip_value = input('Enter zipcode: ')
            if zip_value.isdigit() != True:
                print('invalid zip entry, re-enter\n')
                continue
            else:
                RawcountryName = input('Enter your country: ')
                countryName = RawcountryName[0:2].lower()
                print('\n')
                print('you are interested in', zip_value, countryName.upper())
                Now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print('Current date and time is:', Now)
                check_weather(cityName='', stateName='', countryName=countryName, zipCode=str(zip_value))
            continue
    else:
        print('invalid entry, re-enter, please only choose from prompted keys \n')
        continue
        
def testcase():
    check_weather(cityName='AA', stateName='B', countryName='us', zipCode='')
    check_weather(cityName='', stateName='', countryName='CN', zipCode='78681')
    
if __name__ == "__main__":
    main()
    #testcase()

