import json
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data")

# LOAD JSON DATA
with open(os.path.join(DATA_DIR, "hotels.json"), "r") as file:
    hotels_data = json.load(file)

# HOTEL SEARCH
def get_hotel(city, preference):
    results = []
    for hotel in hotels_data:
        if hotel['city'].lower() == city.lower():
            results.append(hotel)
    if not results:
        return 'Hotel not found'
    if preference.lower() == 'cheap':   
        selected_hotel = min(results,key=lambda x: (x['price_per_night']))
    else:
        selected_hotel = max(results, key=lambda x: (x["stars"],-x["price_per_night"]))
    return selected_hotel