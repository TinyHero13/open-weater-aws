import requests
from airflow.models import Variable

def extract():
    API_KEY = Variable.get("OPENWEATHER_API_KEY")

    cities = ['Rio de Janeiro', 'Belford Roxo', 'Nova Iguaçu']
    temp_list = []

    for city in cities:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(base_url, params=params).json()
        temp_list.append(response)

    return temp_list