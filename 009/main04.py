travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

def add_new_country(country_in, total_visits_in, cities_visited_in):
    new_entry = {}
    new_entry = {
        "country": country_in,
        "cities_visited": cities_visited_in,
        "total_visits": total_visits_in
    }
    # alternative
    # new_entry["country"] = country_in
    # new_entry["cities_visited"] = cities_visited_in
    # new_entry["total_visits"] = total_visits_in
    
    travel_log.append(new_entry)

#main program
add_new_country(country_in="Russia", total_visits_in=2, cities_visited_in=["Moscow", "Saint Petesburg"])

print(travel_log)