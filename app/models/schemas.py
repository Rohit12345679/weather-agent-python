from pydantic import BaseModel


class WeatherRequest(BaseModel):
    city: str


class WeatherResponse(BaseModel):
    response: str