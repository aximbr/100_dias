import requests
#import os

#BEARER = os.getenv("API_Bearer_Sheety_Repl.it")
BEARER = "TryToGuessHowEasy"
#USERNAME = os.getenv("API_Username_Sheety")
USERNAME = "0ae3ba4e02da96577e65ec9931229be4"
PROJECT = "flightDeals"
SHEET = "users"

base_url = "https://api.sheety.co"

def post_new_row(first_name, last_name, email):
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url


    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=url, json=body)
    response.raise_for_status()
    print(response.text)