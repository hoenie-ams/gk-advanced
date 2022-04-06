"""
Demo of API calls
"""

import requests

city = "Amsterdam"

url = f"https://www.metaweather.com/api/location/search/?query={city}"
print(url)

r = requests.get(url).json()
woeid = r[0]["woeid"]

weather_url = f"https://www.metaweather.com/api/location/{woeid}"
r = requests.get(weather_url).json()
print(r)
