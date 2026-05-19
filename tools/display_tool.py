from datetime import datetime, timedelta


# DISPLAY OUTPUT
def display_trip(trip):

    print("\n")

    print("=" * 50)

    days = trip.get("days", 3)
    city = trip.get("destination", "Unknown")

    print(f"      Your {days}-Day Trip to {city}")

    print("=" * 50)

    # ---------------- FLIGHT ----------------
    flight = trip.get("flight")

    if flight and isinstance(flight, dict):

        print("\nFlight Selected:")

        print(
            f"- {flight['airline']} "
            f"(₹{flight['price']})"
        )

    # ---------------- HOTEL ----------------
    hotel = trip.get("hotel")

    if hotel and isinstance(hotel, dict):

        print("\nHotel Booked:")

        print(
            f"- {hotel['name']} "
            f"(₹{hotel['price_per_night']}/night, "
            f"{hotel['stars']}-star)"
        )

    # ---------------- WEATHER ----------------
    weather = trip.get("weather")

    if weather and isinstance(weather, dict):

        print("\nWeather:")

        for i in range(days):

            print(
                f"- Day {i+1}: "
                f"{weather.get('weather', 'Clear')} "
                f"({weather.get('temperature', 'N/A')}°C)"
            )

    # ---------------- ITINERARY ----------------
    itinerary = trip.get("itinerary")

    if itinerary:

        print("\nItinerary:")

        for item in itinerary:

            print(
                f"Day {item['day']}: "
                f"{item['activity']}"
            )

    # ---------------- BUDGET ----------------
    print("\nEstimated Total Budget:")

    flight_price = 0
    hotel_price = 0

    if flight and isinstance(flight, dict):
        flight_price = flight["price"]

    if hotel and isinstance(hotel, dict):
        hotel_price = (
            hotel["price_per_night"]
            * days
        )

    food_cost = 2000

    print(f"- Flight: ₹{flight_price}")
    print(f"- Hotel: ₹{hotel_price}")
    print(f"- Food & Travel: ₹{food_cost}")

    print("-" * 40)

    print(
        f"Total Cost: ₹{trip['total_cost']}"
    )

    print("\n")