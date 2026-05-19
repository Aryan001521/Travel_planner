import json
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data")

# LOAD JSON DATA
with open(os.path.join(DATA_DIR, "flights.json"), "r") as file:
    flights_data = json.load(file)

# FLIGHT SEARCH
def get_flight(from_city, to_city, preference):
    results = []
    for flight in flights_data:
        if (
            flight['from'].lower() == from_city.lower()
            and
            flight['to'].lower() == to_city.lower()
        ):
            results.append(flight)
    if  not results:
        return 'Flight not found'
    if preference.lower() == 'cheap':
          best_flight = min(results,key=lambda x: x['price'])  
    else:
          best_flight = max(results,key = lambda x:x['price'])
    return best_flight
         