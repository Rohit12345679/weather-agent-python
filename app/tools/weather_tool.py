from langchain.tools import tool

from app.services.weather_service import get_weather


@tool
def weather_tool(city: str) -> str:
    """
    Get weather of a city.
    """

    data = get_weather(city)

    if data.get("cod") != 200:
        return "Weather not found."

    return (
        f"City : {city}\n"
        f"Temperature : {data['main']['temp']}°C\n"
        f"Humidity : {data['main']['humidity']}%\n"
        f"Condition : {data['weather'][0]['description']}"
    )