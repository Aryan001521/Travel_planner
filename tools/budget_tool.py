# BUDGET CALCULATION
def calculate_total_cost(flight, hotel, days):

    total_cost = 0

    valid_trip = False

    # FLIGHT COST
    if (
        flight
        and isinstance(flight, dict)
        and flight.get("price")
    ):

        total_cost += flight["price"]
        valid_trip = True

    # HOTEL COST
    if (
        hotel
        and isinstance(hotel, dict)
        and hotel.get("price_per_night")
    ):

        total_cost += (
            hotel["price_per_night"] * days
        )

        valid_trip = True

    # EXTRA EXPENSES
    if valid_trip:

        food_and_transport = 2000
        total_cost += food_and_transport

    return total_cost
