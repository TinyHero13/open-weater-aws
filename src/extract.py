import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract():
    API_KEY = os.getenv('OPENWEATHER_API_KEY') 

    city = ['Rio de Janeiro', 'Sao Paulo']
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params).json()
    
    return response