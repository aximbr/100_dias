import requests

URL = "https://pixe.la/v1/users"

users_param = {
    "token" : "python_user",
    "username" : "yabadabadu",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
        }

response = requests.post(url=URL, json=users_param)

print(response.text)