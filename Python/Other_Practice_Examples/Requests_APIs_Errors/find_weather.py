import requests

# Get location from user
# Use location as a query for location web API request
Get WOEID from location API web request to get weather info
Convert the weather info to a python dictionary and print 


API_BASE= 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'

list_of_cities = requests.get(API_BASE + API_LOCATION)

def fetch_location():
    query = input("What is your location? ")
    if len(query) == 0:
        print(f"Sorry, I don't know where that is. Is it one of these places:\n{list_of_cities}")
    location = requests.get(API_BASE + API_LOCATION + query).json()


def fetch_weather():
    woeid = location[0]['woeid']
    weather = requests.get(API_BASE + API_WEATHER + str(woeid)).json()

