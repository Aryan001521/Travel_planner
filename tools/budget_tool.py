 #BUDGET CALCULATION
def calculate_total_cost(flight, hotel, days):
    total_cost = 0
    # Flight Cost
    if flight and isinstance(flight, dict):
        total_cost += flight['price']
    # Hotel Cost
    if hotel and isinstance(hotel, dict):
        total_cost += (hotel['price_per_night'] * days)
    # Extra expenses
    food_and_transport = 2000
    total_cost += food_and_transport
    return total_cost
