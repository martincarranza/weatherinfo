import requests
from pprint import pprint

API_Key = '307eb52d86b40b12933a36d1b8c42eaf'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)