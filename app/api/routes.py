from fastapi import APIRouter

from app.agents.weather_agent import ask_agent
from app.models.schemas import WeatherRequest

router = APIRouter()


@router.post("/weather")
def weather(request: WeatherRequest):

    answer = ask_agent(request.city)

    return {
        "response": answer
    }