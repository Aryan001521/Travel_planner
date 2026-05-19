import streamlit as st
from agent.travel_agent import process_travel_query

# PAGE CONFIG
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    border: 1px solid #334155;
    padding: 12px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #2563eb, #7c3aed);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(to right, #1d4ed8, #6d28d9);
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 10px rgba(255,255,255,0.05);
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    "<div class='title'>✈️ AI Travel Planner</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Plan Smart Trips with AI + LangChain + Gemini</div>",
    unsafe_allow_html=True
)

# LAYOUT
col1, col2 = st.columns(2)

with col1:

    from_city = st.text_input(
        "From City",
        placeholder="Delhi"
    )

with col2:

    to_city = st.text_input(
        "Destination City",
        placeholder="Goa"
    )

# DAYS
days = st.slider(
    "Select Number of Days",
    min_value=1,
    max_value=15,
    value=3
)

# TRIP TYPE
preference = st.selectbox(
    "Select Trip Type",
    ["cheap", "luxury"]
)

# BUTTON
if st.button("Generate Travel Plan"):

    if from_city and to_city:

        query = (
            f"{from_city} to {to_city} "
            f"{days} day trip "
            f"in {preference}"
        )

        with st.spinner("Planning your dream trip..."):

            try:

                trip = process_travel_query(query)

                st.success("Trip Generated Successfully!")

                # FLIGHT
                flight = trip.get("flight")

                if flight and isinstance(flight, dict):

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.subheader("✈️ Flight Selected")

                    st.write(
                        f"**Airline:** {flight['airline']}"
                    )

                    st.write(
                        f"**From:** {flight['from']}"
                    )

                    st.write(
                        f"**To:** {flight['to']}"
                    )

                    st.write(
                        f"**Price:** ₹{flight['price']}"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                # HOTEL
                hotel = trip.get("hotel")

                if hotel and isinstance(hotel, dict):

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.subheader("🏨 Hotel Recommendation")

                    st.write(
                        f"**Name:** {hotel['name']}"
                    )

                    st.write(
                        f"**Stars:** ⭐ {hotel['stars']}"
                    )

                    st.write(
                        f"**Price/Night:** ₹{hotel['price_per_night']}"
                    )

                    st.write(
                        f"**Amenities:** "
                        f"{', '.join(hotel['amenities'])}"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                # PLACES
                places = trip.get("places")

                if places:

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.subheader("🏝️ Top Places")

                    for place in places["top_places"]:

                        st.write(
                            f"📍 {place['name']} "
                            f"(⭐ {place['rating']})"
                        )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                # WEATHER
                weather = trip.get("weather")

                if weather and isinstance(weather, dict):

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.subheader("🌤️ Weather Forecast")

                    st.write(
                        f"**Temperature:** "
                        f"{weather['temperature']}°C"
                    )

                    st.write(
                        f"**Wind Speed:** "
                        f"{weather['windspeed']} km/h"
                    )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                # ITINERARY
                itinerary = trip.get("itinerary")

                if itinerary:

                    st.markdown(
                        "<div class='card'>",
                        unsafe_allow_html=True
                    )

                    st.subheader("🗓️ Day-wise Itinerary")

                    for day in itinerary:

                        st.write(f"### {day['day']}")

                        st.write(
                            f"📍 {day['place']}"
                        )

                        st.write(
                            f"📝 {day['plan']}"
                        )

                    st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                    )

                # BUDGET
                st.markdown(
                    "<div class='card'>",
                    unsafe_allow_html=True
                )

                st.subheader("💰 Estimated Budget")

                st.write(
                    f"## ₹{trip['total_cost']}"
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning(
            "Please enter both cities."
        )