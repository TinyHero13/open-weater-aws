import pandas as pd
from datetime import datetime, timedelta, timezone

def transform(task_id, **kwargs):
    ti = kwargs['ti']
    temp_list = ti.xcom_pull(task_ids=task_id) 
    
    rows = []

    for item in temp_list:
        coord = item['coord']
        lon = coord['lon']
        lat = coord['lat']
        
        for weather in item['weather']:
            main = weather['main']
            description = weather['description']
            
            main_data = item['main']
            temp = main_data['temp']
            feels_like = main_data['feels_like']
            temp_min = main_data['temp_min']
            temp_max = main_data['temp_max']
            pressure = main_data['pressure']
            humidity = main_data['humidity']

            rows.append({
                'lon': lon,
                'lat': lat,
                'main': main,
                'description': description,
                'temp': temp,
                'feels_like': feels_like,
                'temp_min': temp_min,
                'temp_max': temp_max,
                'pressure': pressure,
                'humidity': humidity,
                'name': item['name'],
                'date': datetime.now(timezone(timedelta(hours=-3)))
            })

    df = pd.DataFrame(rows)

    return df