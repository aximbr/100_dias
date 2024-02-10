import requests
import datetime as dt

URL="https://api.weatherapi.com/v1/forecast.json"

#The key was modified and not work
MY_KEY= "1e8a23e877d741dba041339362410XX"
MY_LAT=-22.097909
MY_LONG=-51.398390
MY_LATLONG = f"{MY_LAT},{MY_LONG}"
CODE_START_RAIN = 1006

parameters= {
    "key" : MY_KEY,
    "q" : MY_LATLONG,
    "days" : 1,
    "aqi" : "no",
    "alerts" : "no"
}

#https://api.weatherapi.com/v1/forecast.json?key=1e8a23e877d741dba041339362410XX&q=-22.097909,-51.398390&days=1&aqi=no&alerts=no

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()

my_location = data["location"]["name"]

this_hour = int(dt.datetime.now().hour)

next_hours_contidion = []

for h in range(0, 24):
    next_hours_contidion.append(data["forecast"]["forecastday"][0]["hour"][h]["condition"]["code"])


need_umbrella = False    
for code in next_hours_contidion[this_hour:24]:
    if code > CODE_START_RAIN:
        need_umbrella = True
        
if need_umbrella:
    print("Bring umbrella!")
    print(next_hours_contidion[this_hour:24])
else:
    print("Enjoy the ride!")
    