# weather_app/api.py
import requests

def get_weather_data(city):
    api_key = 'django-insecure-dy*2hdvj0188oahi&q^s3wh4g6zku&7%tbx6i(wc$m!0c2of5w'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

