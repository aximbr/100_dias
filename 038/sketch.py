# APP_ID = "xpto"
# API_KEY = "abcd"
import requests

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = "9fa3007f"
NUTRITIONIX_APP_KEY = "c00ce89c396f38d2c0ce44add9849537"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
    "Content-Type": "application/json",
}

nutritionix_data = {
    "query": input("What did you do? :"),
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 178,
    "age": 43,
}

response = requests.post(NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_data)
response.raise_for_status()
print(response.json())