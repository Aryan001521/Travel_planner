import asyncio

try:
    loop = asyncio.get_event_loop()

except RuntimeError:

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

import os
import sys
import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage

# ROOT DIRECTORY
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# IMPORT TOOLS
from tools.flight_tool import get_flight
from tools.hotel_tool import get_hotel
from tools.place_tool import get_place
from tools.weather_tool import get_wheather
from tools.budget_tool import calculate_total_cost
from tools.display_tool import display_trip
from tools.itternative_tool import generate_itinerary

# LOAD ENV
load_dotenv()

# GEMINI MODEL
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


def process_travel_query(user_input: str):

    system_msg = """
You are a helpful travel assistant.

Extract travel information from user query.

Return ONLY valid JSON.

Fields:
- from_city
- to_city
- preference
- days
- start_date
- needs

Rules:
- preference can be "cheap" or "luxury"
- default preference = "cheap"
- default days = 3

needs can contain:
["flights", "hotels", "places", "budget"]

Example:
{
    "from_city":"Hyderabad",
    "to_city":"Delhi",
    "preference":"cheap",
    "days":5,
    "start_date":"2026-06-12",
    "needs":["flights","hotels","places","budget"]
}
"""

    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_input)
    ]

    # LLM RESPONSE
    response = llm.invoke(messages)

    try:

        content = response.content

        # JSON EXTRACTION
        start_idx = content.find("{")
        end_idx = content.rfind("}") + 1

        if start_idx == -1 or end_idx == 0:
            print("Could not parse query.")
            return None

        json_str = content[start_idx:end_idx]

        travel_info = json.loads(json_str)

    except Exception as e:
        print(f"JSON Parsing Error: {e}")
        return None

    # EXTRACT VALUES
    from_city = travel_info.get("from_city")
    to_city = travel_info.get("to_city")
    preference = travel_info.get("preference", "cheap")
    days = travel_info.get("days", 3)
    start_date = travel_info.get("start_date")

    # ---------------- FLIGHT ----------------
    flight = None

    if (
        from_city
        and to_city
    ):

        flight = get_flight(
            from_city,
            to_city,
            preference
        )

    # ---------------- HOTEL ----------------
    hotel = None

    if to_city:

        hotel = get_hotel(
            to_city,
            preference
        )

    # ---------------- PLACES ----------------
    places = None

    if to_city:

        best_place, top_places = get_place(to_city)

        places = {
            "best_place": best_place,
            "top_places": top_places
        }

    # ---------------- WEATHER ----------------
    weather = None

    if to_city:

        weather = get_wheather(to_city)

    # ---------------- ITINERARY ----------------
    itinerary = []

    if places:

        itinerary = generate_itinerary(
            places,
            days
        )

    # ---------------- BUDGET ----------------
    total_budget = calculate_total_cost(
        flight,
        hotel,
        days
    )

    # ---------------- FINAL TRIP OBJECT ----------------
    trip = {
        "destination": to_city,
        "days": days,
        "start_date": start_date,
        "flight": flight,
        "hotel": hotel,
        "places": places,
        "weather": weather,
        "itinerary": itinerary,
        "total_cost": total_budget
    }

    return trip


# MAIN
if __name__ == "__main__":

    user_input = input("Ask your travel query: ")

    trip = process_travel_query(user_input)

    if trip:

        display_trip(trip)

    else:

        print("Trip generation failed.")