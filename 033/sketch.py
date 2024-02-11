import requests

# URL="http://api.open-notify.org/iss-now.json"

# response = requests.get(url=URL)
# response.raise_for_status()

# data = response.json()["iss_position"]

# longitude = float(data["longitude"])
# latitude = float(data["latitude"])

# iss_postion = (latitude, longitude)

# print(iss_postion)
import datetime as dt 

MY_LAT=-22.097909
MY_LONG=-51.398390

URL = "https://api.sunrise-sunset.org/json"

now = dt.datetime.now()
hour_now = now.hour
print(hour_now)

parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise = sunrise.split("T")
sunset = sunset.split("T")

sunrise_hour = sunrise[1][0:2]
sunset_hour = sunset[1][0:2]

print(sunrise_hour)
print(sunset_hour)