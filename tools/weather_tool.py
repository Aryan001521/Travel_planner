import requests


def get_wheather(city):

    try:

        # GEO API
        geo_url = (
            f"https://geocoding-api.open-meteo.com/v1/search?"
            f"name={city}&count=1"
        )

        geo_response = requests.get(geo_url)

        geo_data = geo_response.json()

        results = geo_data.get("results")

        if not results:
            return {
                "city": city,
                "temperature": "N/A",
                "windspeed": "N/A",
                "weather": "City not found"
            }

        latitude = results[0]["latitude"]
        longitude = results[0]["longitude"]

        # WEATHER API
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}"
            f"&longitude={longitude}"
            f"&current_weather=true"
        )

        weather_response = requests.get(weather_url)

        weather_data = weather_response.json()

        current_weather = weather_data.get(
            "current_weather",
            {}
        )

        # WEATHER CODE
        weather_code = current_weather.get(
            "weathercode",
            -1
        )

        # WEATHER MAP
        weather_map = {
            0: "Clear Sky",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Cloudy",
            45: "Fog",
            48: "Depositing Rime Fog",
            51: "Light Drizzle",
            61: "Rain",
            71: "Snow"
        }

        condition = weather_map.get(
            weather_code,
            "Unknown"
        )

        return {
            "city": city,
            "temperature": current_weather.get(
                "temperature"
            ),
            "windspeed": current_weather.get(
                "windspeed"
            ),
            "weather": condition
        }

    except Exception as e:

        return {
            "city": city,
            "temperature": "N/A",
            "windspeed": "N/A",
            "weather": f"API Error: {e}"
        }