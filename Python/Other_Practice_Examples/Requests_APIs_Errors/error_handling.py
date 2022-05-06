# Import request module to make requests using python
import requests

# Write a request that results in an exception


try:
    request = requests.get('https://www.google.com')
    print(request)
except requests.exceptions.ConnectionError:
        print("Could not connect to server.")


