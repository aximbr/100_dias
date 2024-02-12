from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

#main()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#print(sheet_data)
#populate with IATA code for all cities in Flight Deals.csv
if sheet_data["IATA Code"][0] == "":
    for row in range(len(sheet_data)):
        sheet_data.loc[row, "IATA Code"] = flight_search.get_destination_code(sheet_data.loc[row,"City"])
   
#print(sheet_data) 
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

#Search for lowest price on destinations and print output
for row in range(len(sheet_data)):
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        sheet_data.loc[row, "IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
#Send SMS if the price is lower than we have on csv file    
    if flight.price < sheet_data.loc[row, "Lowest Price"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )
