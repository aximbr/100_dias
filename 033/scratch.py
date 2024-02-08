import requests

URL="http://api.open-notify.org/iss-now.json"

response = requests.get(url=URL)
response.raise_for_status()

data = response.json()["iss_position"]

longitude = float(data["longitude"])
latitude = float(data["latitude"])

iss_postion = (latitude, longitude)

print(iss_postion)