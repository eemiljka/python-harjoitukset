import requests

API_key = "9f27369183880d8c5a9e9d0f84c41d98"

city = input("Enter a city or press 'Enter' to quit program: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q"+city
weather_data = requests.get(base_url).json()
print(weather_data)

#TODO: venaa, että API key toimii ja sitten koodaa loppuun.