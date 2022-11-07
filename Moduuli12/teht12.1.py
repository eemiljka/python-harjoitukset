import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)
json_response = response.json()

print(json_response["value"])