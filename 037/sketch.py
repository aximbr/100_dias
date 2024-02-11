import requests

TOKEN = "python_user"
USERNAME = "yabadabadu"
PIXELA = "https://pixe.la/v1/users"

# users_param = {
#     "token" : TOKEN,
#     "username" : USERNAME,
#     "agreeTermsOfService" : "yes",
#     "notMinor" : "yes",
#         }

# response = requests.post(url=PIXELA, json=users_param)

# print(response.text)

graph_endpoint = f"{PIXELA}/{USERNAME}/graphs"

graph_params = {
    "id" : "graph1",
    "name" : "My Python Study Hours",
    "unit" : "hrs",
    "type" : "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

print(response.text)

#to test use: https://pixe.la/v1/users/yabadabadu/graphs/graph1.html
