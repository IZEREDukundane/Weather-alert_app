import requests

def get_weather(location):
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()  # Will return the weather data as a dictionary

