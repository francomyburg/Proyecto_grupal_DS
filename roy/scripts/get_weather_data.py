import requests
from tqdm import tqdm
import pandas as pd

# Funcion para descargar la data del clima
def get_weather_data(dataframe, start_date, end_date):
    url = 'https://archive-api.open-meteo.com/v1/archive'
    columns = ['latitude', 'longitude', 'temperature_2m', 'relativehumidity_2m', 'precipitation', 'rain', 'windspeed_10m']
    df = pd.DataFrame(columns=columns)
    
    for index, row in tqdm(dataframe.iterrows(), total=dataframe.shape[0], desc='Downloading weather data'):
        params = {
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'start_date': start_date,
            'end_date': end_date,
            'hourly': ['temperature_2m', 'relativehumidity_2m', 'precipitation', 'rain', 'windspeed_10m']
        }
        try:
            res = requests.get(url, params=params)
            if res.status_code == 200:
                data = res.json()
                hourly_data = pd.DataFrame.from_dict(data['hourly'])
                hourly_data['latitude'] = row['latitude']
                hourly_data['longitude'] = row['longitude']
                df = pd.concat([df, hourly_data], ignore_index=True)
            else:
                print(f"Peticion fallida para el registro {index}: {res.status_code}")
        except Exception as e:
            print(f"Error al descargar la data para el registro {index}: {str(e)}")

    return df
