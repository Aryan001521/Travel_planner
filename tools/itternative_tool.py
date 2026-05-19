def generate_itinerary(places, days):

    itinerary = []

    if not places:

        return itinerary

    top_places = places.get("top_places", [])

    if not top_places:

        return itinerary

    for i in range(days):

        place = top_places[i % len(top_places)]

        itinerary.append({

            "day": f"Day {i + 1}",

            "place": place["name"],

            "plan": (
                f"Visit {place['name']} "
                f"and enjoy sightseeing."
            )
        })

    return itinerary