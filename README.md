# ✈️ AI Travel Planner

An AI-powered Travel Planning Web Application built using **Python, Streamlit, LangChain, and Gemini AI**.  
The system generates complete travel plans including flights, hotels, tourist places, weather details, itinerary, and estimated budget.

---

# 📌 Project Overview

AI Travel Planner helps users generate smart and personalized travel plans by entering:

- Source City
- Destination City
- Number of Days
- Trip Type (Cheap / Luxury)

The application uses AI to process user queries and generate a complete travel itinerary automatically.

---

# 🚀 Features

- AI-Based Travel Planning
- Flight Recommendations
- Hotel Suggestions
- Tourist Place Recommendations
- Weather Forecast
- Day-wise Itinerary Generation
- Estimated Budget Calculation
- Modern Streamlit UI
- Error Handling for Invalid Cities

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | Web Application UI |
| LangChain | AI Workflow |
| Gemini API | AI Response Generation |
| JSON | Local Data Storage |
| Requests API | Weather Data |

---

# 📂 Project Structure

```bash
travel_planner/
│
├── agent/
│   └── travel_agent.py
│
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── place_tool.py
│   ├── weather_tool.py
│   ├── budget_tool.py
│   ├── itternative_tool.py
│   └── display_tool.py
│
├── data/
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
├── main.py
├── requirements.txt
└── README.md
