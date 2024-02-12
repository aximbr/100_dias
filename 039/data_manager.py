# from pprint import pprint
# import requests

# SHEETY_PRICES_ENDPOINT = "YOUR SHEETY PRICES ENDPOINT"


# class DataManager:

#     def __init__(self):
#         self.destination_data = {}

#     def get_destination_data(self):
#         response = requests.get(url=SHEETY_PRICES_ENDPOINT)
#         data = response.json()
#         self.destination_data = data["prices"]
#         return self.destination_data

#     def update_destination_codes(self):
#         for city in self.destination_data:
#             new_data = {
#                 "price": {
#                     "iataCode": city["iataCode"]
#                 }
#             }
#             response = requests.put(
#                 url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
#                 json=new_data
#             )
#             print(response.text)
import pandas
CSV_FILE = "Flight Deals.csv"
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        file_csv = pandas.read_csv(CSV_FILE, na_filter=False)
        data = file_csv.to_dict(orient="list")
        self.destination_data = data
        return self.destination_data

    def update_destination_codes(self):
        for City in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": City["iataCode"]
                }
            }
            print(new_data)
            # response = requests.put(
            #     url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
            #     json=new_data
            # )
            # print(response.text)