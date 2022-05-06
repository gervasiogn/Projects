import requests

city = input("Which city are you in? ").lower()

# Returns response object
city_info = requests.get(f'https://www.metaweather.com/api/location/search/?query={city}')

# Converts json response object into python dictionary
details = city_info.json()

# get woeid number to use in weather request
woeid = details[0]['woeid']

# Returns weather report as python dictionary
weather_report = requests.get(f'https://www.metaweather.com/api/location/{woeid}').json()

for x in weather_report['consolidated_weather']:
    print(x)
