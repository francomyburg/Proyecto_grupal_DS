# Gestion de rutas
import utils.paths as path

# Importacion de librerías
import pandas as pd
import numpy as np
import requests
import os

# Directorio de los datos crudos / raw data
raw_data_dir = path.make_dir_function(['datasets', 'raw'])
proc_data_dir = path.make_dir_function(['datasets', 'processed'])



#----------------------------------------------------------#
# Funcion para descargar el dataset Contaminación Acústica
#----------------------------------------------------------#

def download_file(url, file_name):
    # Ruta para guardar el archivo
    file_path = raw_data_dir(raw_data_dir(), file_name)
    try:
        # Solicitud GET para descargar el archivo
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"{file_name} ha sido descargado y guardado en {raw_data_dir()}")
        else:
            print(f"No se pudo descargar {file_name}. El código de estado de la solicitud es {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"No se pudo descargar {file_name}. Se produjo un error de red: {e}")

#------------------------------#
# Funcion para descargar 
#------------------------------#

if __name__ == '__main__':
    # URL del dataset
    NOISE_POLLUTION_URL = "https://zenodo.org/record/3966543/files/annotations.csv?download=1"
    # Descargar el dataset
    download_file(NOISE_POLLUTION_URL, 'noise_pollution.csv')
    