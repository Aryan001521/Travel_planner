from langchain.tools import StructuredTool
from tools.flight_tool import get_flight
from tools.hotel_tool import get_hotel
from tools.place_tool import get_place

def flight_search(from_city: str, to_city: str, preference: str = 'cheap') -> str:
    """
    Find flights between two cities.
    
    Args:
        from_city: Departure city name (e.g., 'Hyderabad')
        to_city: Destination city name (e.g., 'Delhi')
        preference: 'cheap' for budget flights or 'luxury' for premium flights
    
    Returns:
        Flight details or error message
    """
    return str(get_flight(from_city, to_city, preference))

def hotel_search(city: str, preference: str = 'cheap') -> str:
    """
    Find hotels in a city.
    
    Args:
        city: City name (e.g., 'Delhi')
        preference: 'cheap' for budget hotels or 'luxury' for premium hotels
    
    Returns:
        Hotel details or error message
    """
    return str(get_hotel(city, preference))

def places_search(city: str) -> str:
    """
    Find top tourist places in a city.
    
    Args:
        city: City name (e.g., 'Delhi')
    
    Returns:
        Top tourist places in the city
    """
    result = get_place(city)
    return str(result)

# Create StructuredTools
flight_tool = StructuredTool.from_function(flight_search)
hotel_tool = StructuredTool.from_function(hotel_search)
places_tool = StructuredTool.from_function(places_search)