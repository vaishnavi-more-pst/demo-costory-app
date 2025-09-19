import requests

API_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(latitude: float, longitude: float) -> dict:
    """
    Fetch current weather data for a given location.

    Args:
        latitude (float): Latitude of the location
        longitude (float): Longitude of the location

    Returns:
        dict: Weather details including temperature and wind speed
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  # raise error if API call fails
    return response.json().get("current_weather", {})


if __name__ == "__main__":
    # Example: New Delhi
    lat, lon = 28.6139, 77.2090
    weather = get_weather(lat, lon)

    if weather:
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")
    else:
        print("Weather data not available.")
