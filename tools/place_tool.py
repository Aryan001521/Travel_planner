import json
import os

# GET CURRENT DIRECTORY
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(
    os.path.dirname(SCRIPT_DIR),
    "data"
)

# LOAD JSON DATA
with open(
    os.path.join(DATA_DIR, "places.json"),
    "r"
) as file:

    places_data = json.load(file)


# PLACE SEARCH
def get_place(city):

    results = []

    for place in places_data:

        if place['city'].lower() == city.lower():

            results.append(place)

    # IF NO PLACE FOUND
    if not results:

        return None, []

    # BEST PLACE
    max_rating_place = max(
        results,
        key=lambda x: x['rating']
    )

    # TOP 3 PLACES
    top_places = sorted(
        results,
        key=lambda x: x['rating'],
        reverse=True
    )[:3]

    return max_rating_place, top_places