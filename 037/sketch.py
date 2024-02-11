import requests
import datetime as dt

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

GRAPH = "graph1"

graph_params = {
    "id" : GRAPH,
    "name" : "My Python Study Hours",
    "unit" : "hrs",
    "type" : "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

#print(response.text)

#to test use: https://pixe.la/v1/users/yabadabadu/graphs/graph1.html

#Add a pixel
#Date must be provide as "YYYYMMDD" string format 
today = dt.datetime.now().strftime("%Y%m%d")
# print(today)

#Quantity is also in string format 
quant = str(10)

pixel_endpoint = f"{PIXELA}/{USERNAME}/graphs/{GRAPH}"

pixel_params = {
    "date" : today,
    "quantity" : quant,   
            }

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

print(response.text)