import json

import requests

from app.services.redis_service import redis_client
from app.config.settings import OPENWEATHER_API_KEY;



def get_weather(city: str):

    key = f"weather:{city.lower()}"

    cached = redis_client.get(key)

    if cached:
        print("Cache Hit")
        return json.loads(cached)

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    redis_client.setex(
            key,
            300,      # 5 minutes
            json.dumps(data)
    )

    return data

      