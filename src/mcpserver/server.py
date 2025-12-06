import requests
from mcp.server.fastmcp import FastMCP
from mcpserver.config import API_KEY

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def get_weather(location: str) -> str:
    """
    Retrieves the real current weather for a specified location.

    Args:
        location: City name, 'city,country', or ZIP code.
    """

    if not API_KEY:
        return "Missing OPENWEATHER_API_KEY environment variable."

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Decide if it's a ZIP code or city
    if location.replace(" ", "").isdigit():
        params = {"zip": location, "appid": API_KEY}
    else:
        params = {"q": location, "appid": API_KEY}

    resp = requests.get(base_url, params=params)
    data = resp.json()

    # Handle errors from OpenWeather
    if data.get("cod") != 200:
        return f"Could not fetch weather for '{location}': {data.get('message')}"

    desc = data["weather"][0]["description"]
    temp_c = round(data["main"]["temp"] - 273.15, 1)
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    city = data["name"]
    country = data["sys"]["country"]

    return (
        f"Weather in {city}, {country}: {desc}. "
        f"{temp_c}°C, humidity {humidity}%, wind {wind} m/s."
    )
