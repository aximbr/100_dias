import requests
import datetime as dt

TOKEN = "python_user"
USERNAME = "yabadabadu"
PIXELA = "https://pixe.la/v1/users"
GRAPH = "graph1"

def create_pixel_user(username, token):
    """Create a new user"""
    users_param = {
        "token" : token,
        "username" : username,
        "agreeTermsOfService" : "yes",
        "notMinor" : "yes",
            }

    response = requests.post(url=PIXELA, json=users_param)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False

def create_pixel_graph(username, token, graph_id, graph_name, type, color):
    """Create a pixel graph"""
    graph_endpoint = f"{PIXELA}/{username}/graphs"

    graph_params = {
        "id" : graph_id,
        "name" : graph_name,
        "unit" : "hrs",
        "type" : type,
        "color": color
            }

    headers = {
        "X-USER-TOKEN" : token
            }

    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False


def add_pixel(username, token, graph_id, date, quant):
    """Add a pixel"""
    pixel_endpoint = f"{PIXELA}/{username}/graphs/{graph_id}"

    pixel_params = {
        "date" : date,
        "quantity" : quant,   
                }
    headers = {
        "X-USER-TOKEN" : token
            }

    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False

def update_pixel(username, token, graph_id, date, new_quant):
    """Update a pixel"""
    update_pixel_endpoint = f"{PIXELA}/{username}/graphs/{graph_id}/{date}"

    update_params = {
        "quantity" : new_quant,   
                }
    headers = {
        "X-USER-TOKEN" : token
            }   
    response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False
    
def delete_pixel(username, token, graph_id, date):
    """Delete a pixel"""
    delete_pixel_endpoint = f"{PIXELA}/{username}/graphs/{graph_id}/{date}"
    headers = {
        "X-USER-TOKEN" : token
            }  

    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    if response.status_code == 200:
        print(response.text)
        return True
    else:
        return False

#main()

#create a user
create_pixel_user(USERNAME, TOKEN)

#create a graph
create_pixel_graph(USERNAME, TOKEN, GRAPH, "My hours with Python", "float", "sora")

#add a pixel to graph
#Date must be provide as "YYYYMMDD" string format 
today = dt.datetime.now().strftime("%Y%m%d")

add_pixel(USERNAME, TOKEN, GRAPH, today, "10")

#update a pixel with new value
update_pixel(USERNAME,TOKEN, GRAPH, today, "20")

#delete a pixel at specific date
delete_pixel(USERNAME, TOKEN, GRAPH, today)
