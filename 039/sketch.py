import pandas

CSV_FILE = "Flight Deals.csv"
destination_data = {}


file_csv = pandas.read_csv(CSV_FILE, na_filter=False)
data = file_csv.to_dict(orient="list")
destination_data = data
print(destination_data)

for record in destination_data:
    new_data = {
        "price": {
            "iataCode": City["IATA Code"]
        }
    }
print(new_data)
# sheet_data = destination_data

# if sheet_data["IATA Code"][0] == "":
#     # for row in sheet_data:
#     #     row["iataCode"] = flight_search.get_destination_code(row["city"])
#     # data_manager.destination_data = sheet_data
#     # data_manager.update_destination_codes()
#     print("YES")