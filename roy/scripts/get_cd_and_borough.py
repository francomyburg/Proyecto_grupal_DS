import requests
import pandas as pd
from shapely.geometry import Point, shape

def get_community_district_and_borough(df, lat_col, lon_col):
    # Descarga los datos de districtos comunitarios y boroughs
    district_url = 'https://data.cityofnewyork.us/resource/jp9i-3b7y.geojson'
    borough_url = 'https://data.cityofnewyork.us/resource/7t3b-ywvw.geojson'
    district_data = requests.get(district_url).json()
    borough_data = requests.get(borough_url).json()

    # Crea un diccionario con los límites geográficos de cada distrito y borough
    districts = {}
    for feature in district_data['features']:
        district = feature['properties']['boro_cd']
        geometry = shape(feature['geometry'])
        districts[district] = geometry

    boroughs = {}
    for feature in borough_data['features']:
        borough = feature['properties']['boro_name']
        geometry = shape(feature['geometry'])
        boroughs[borough] = geometry

    # Crea una nueva columna para el distrito comunitario y el borough correspondientes a cada punto
    df['community_district'] = None
    df['borough'] = None

    # Compara las coordenadas de cada punto con los límites geográficos de cada distrito y borough para determinar a cuál pertenece
    for i, row in df.iterrows():
        point = Point(row[lon_col], row[lat_col])
        for district, geometry in districts.items():
            if point.within(geometry):
                df.at[i, 'community_district'] = district
                break
        for borough, geometry in boroughs.items():
            if point.within(geometry):
                df.at[i, 'borough'] = borough
                break

    return df
