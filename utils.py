from config import API_KEY
import requests


def weather_by_city(city_name: str) -> float | None:
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': API_KEY,
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'

    }

    try:
        result = requests.get(weather_url, params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]['temp_C']
                except (IndexError, TypeError):
                    return None
        return weather
    except (requests.RequestException):
        return None
