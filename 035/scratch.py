import requests

URL="https://api.openweathermap.org/data/2.5/weather"

#The onecall API does not work with free subscription
URL2="https://api.openweathermap.org/data/2.5/onecall"

MY_KEY= "df81b375a67553f9bc6147884a0d280a"
MY_LAT=-22.097909
MY_LONG=-51.398390

parameters= {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "units" : "metric",
    "appid" : MY_KEY
}

#https://api.openweathermap.org/data/2.5/weather?lat=-22.097909&lon=-51.398390&appid=df81b375a67553f9bc6147884a0d280a

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()

print(data)