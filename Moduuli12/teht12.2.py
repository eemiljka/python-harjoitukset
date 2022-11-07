# This program asks the user a city then prints that city's temperature using API.
import requests

API_key = "9f27369183880d8c5a9e9d0f84c41d98"

city = input("Enter a city or press 'Enter' to quit program: ")
request = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_key

response = requests.get(request)
json_response = response.json()
x = response.json()
y = x["main"]
temperature = y["temp"]

print(city, "temperature is", temperature - 273.15, "celsius at this moment")