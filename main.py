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

body {
    background-color: #0f172a;
}

.main {
    background-color: #0f172a;
    color: white;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

.stTextInput > div > div > input {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
    border: 1px solid #334155;
    padding: 12px;
}

.stSelectbox > div > div {
    background-color: #1e293b;
    color: white;
    border-radius: 12px;
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
    color: white;
}

.card {
    background-color: #1e293b;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 15px rgba(255,255,255,0.05);
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.place-box {
    background-color: #0f172a;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #334155;
}

.itinerary-box {
    background-color: #0f172a;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
    border-left: 5px solid #7c3aed;
}

.budget-box {
    text-align: center;
    padding: 25px;
    background: linear-gradient(to right, #2563eb, #7c3aed);
    border-radius: 20px;
    color: white;
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

# INPUT SECTION
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

                if not trip:

                    st.error("Trip generation failed.")
                    st.stop()

                st.success("Trip Generated Successfully!")

                # ---------------- FLIGHT ----------------

                flight = trip.get("flight")

                if flight and isinstance(flight, dict):

                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.subheader("✈️ Flight Details")

                    st.write(f"**Airline:** {flight.get('airline', 'N/A')}")
                    st.write(f"**From:** {flight.get('from', 'N/A')}")
                    st.write(f"**To:** {flight.get('to', 'N/A')}")
                    st.write(f"**Price:** ₹{flight.get('price', 'N/A')}")

                    st.markdown("</div>", unsafe_allow_html=True)

                # ---------------- HOTEL ----------------

                hotel = trip.get("hotel")

                if hotel and isinstance(hotel, dict):

                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.subheader("🏨 Hotel Recommendation")

                    st.write(f"**Name:** {hotel.get('name', 'N/A')}")
                    st.write(f"**Stars:** ⭐ {hotel.get('stars', 'N/A')}")
                    st.write(
                        f"**Price/Night:** ₹{hotel.get('price_per_night', 'N/A')}"
                    )

                    amenities = hotel.get("amenities", [])

                    if amenities:
                        st.write(
                            f"**Amenities:** {', '.join(amenities)}"
                        )

                    st.markdown("</div>", unsafe_allow_html=True)

                # ---------------- PLACES ----------------

                places = trip.get("places")

                if (
                    places
                    and isinstance(places, dict)
                    and places.get("top_places")
                ):

                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.subheader("🏝️ Top Places")

                    for place in places["top_places"]:

                        st.markdown(
                            f"""
                            <div class='place-box'>
                            📍 <b>{place.get('name', 'Unknown')}</b>
                            <br>
                            ⭐ Rating: {place.get('rating', 'N/A')}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown("</div>", unsafe_allow_html=True)

                # ---------------- WEATHER ----------------

                weather = trip.get("weather")

                if weather and isinstance(weather, dict):

                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.subheader("🌤️ Weather Forecast")

                    temp = weather.get("temperature", "N/A")
                    wind = weather.get("windspeed", "N/A")

                    st.write(f"**Temperature:** {temp}°C")
                    st.write(f"**Wind Speed:** {wind} km/h")

                    st.markdown("</div>", unsafe_allow_html=True)

                # ---------------- ITINERARY ----------------

                itinerary = trip.get("itinerary")

                if itinerary and isinstance(itinerary, list):

                    st.markdown("<div class='card'>", unsafe_allow_html=True)

                    st.subheader("🗓️ Day-wise Itinerary")

                    for day in itinerary:

                        st.markdown(
                            f"""
                            <div class='itinerary-box'>

                            <h4>{day.get('day', 'Day')}</h4>

                            📍 <b>
                            {day.get('place', 'No Place')}
                            </b>

                            <br><br>

                            📝 {day.get('plan', 'No Plan Available')}

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.markdown("</div>", unsafe_allow_html=True)

                # ---------------- BUDGET ----------------

                st.markdown("<div class='card'>", unsafe_allow_html=True)

                st.subheader("💰 Estimated Budget")

                st.markdown(
                    f"""
                    <div class='budget-box'>
                        <h1>₹{trip.get('total_cost', 0)}</h1>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please enter both cities.")
