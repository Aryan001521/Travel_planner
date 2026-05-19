import os
import sys
import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from tools.flight_tool import get_flight
from tools.hotel_tool import get_hotel
from tools.place_tool import get_place

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

def process_travel_query(user_input: str):
    """Process travel query using simple LLM prompting"""
    
    system_msg = """You are a helpful travel booking assistant. Based on the user's query, extract travel information.
Respond with ONLY a JSON object (no extra text) with these fields:
- from_city: departure city
- to_city: destination city  
- preference: "cheap" or "luxury" (default "cheap")
- needs: list of ["flights", "hotels", "places"]

Example: {"from_city":"Hyderabad","to_city":"Delhi","preference":"cheap","needs":["flights","hotels","places"]}"""
    
    messages = [
        SystemMessage(content=system_msg),
        HumanMessage(content=user_input)
    ]
    
    response = llm.invoke(messages)
    
    try:
        # Extract JSON from response
        content = response.content
        start_idx = content.find('{')
        end_idx = content.rfind('}') + 1
        if start_idx == -1 or end_idx == 0:
            return "I couldn't parse your query. Please specify: from_city, to_city, and preference (cheap/luxury)."
        
        json_str = content[start_idx:end_idx]
        travel_info = json.loads(json_str)
    except Exception as e:
        return f"Error parsing response: {e}"
    
    results = []
    
    # Get flights
    if travel_info.get("from_city") and travel_info.get("to_city") and "flights" in travel_info.get("needs", []):
        from_city = travel_info["from_city"]
        to_city = travel_info["to_city"]
        preference = travel_info.get("preference", "cheap")
        
        flight = get_flight(from_city, to_city, preference)
        results.append(f"\n✈️ FLIGHT RESULTS:\n{flight}")
    
    # Get hotel
    if travel_info.get("to_city") and "hotels" in travel_info.get("needs", []):
        to_city = travel_info["to_city"]
        preference = travel_info.get("preference", "cheap")
        
        hotel = get_hotel(to_city, preference)
        results.append(f"\n🏨 HOTEL RESULTS:\n{hotel}")
    
    # Get places
    if travel_info.get("to_city") and "places" in travel_info.get("needs", []):
        to_city = travel_info["to_city"]
        
        places = get_place(to_city)
        results.append(f"\n🏛️ TOP PLACES:\n{places}")
    
    return "\n".join(results) if results else "Could not find travel information for your query."

if __name__ == "__main__":
    user_input = input("Ask your travel query: ")
    response = process_travel_query(user_input)
    print("\n===== TRAVEL ASSISTANT RESPONSE =====\n")
    print(response),