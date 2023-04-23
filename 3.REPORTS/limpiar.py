# %% [markdown]
# ## Limpiar

# %% [markdown]
# ### Amarillos

# %%
def columnas_amarillo(dataframe):

    import numpy as np
    import pandas as pd

    '''Eliminar columnas indeseadas.'''

    try:
        dataframe.drop(columns = ['VendorID', 'RatecodeID', 'store_and_fwd_flag'], inplace = True)
        print('Se eliminaron las columnas: VendorID, RatecodeID', 'store_and_fwd')
        
    except KeyError:
        return 'No están las columnas en el DataFrame.'

# %%
def dt_amarillo(dataframe):
    '''Separar columnas datetime en día y hora.'''

    import numpy as np
    import pandas as pd

    try:
        #Insertar 'pickup_day'.
        dataframe.insert(0, 'pickup_day', dataframe['tpep_pickup_datetime'].dt.date)
        #Insertar 'pickup_time'.
        dataframe.insert(1, 'pickup_time', dataframe['tpep_pickup_datetime'].dt.time)
        #Insertar 'dropoff_day'.
        dataframe.insert(2, 'dropoff_day', dataframe['tpep_dropoff_datetime'].dt.date)
        #Insertar 'dropoff_time'.
        dataframe.insert(3, 'dropoff_time', dataframe['tpep_dropoff_datetime'].dt.time)
        #Eliminar 'tpep_pickup_datetime' y 'tpep_dropoff_datetime'.
        dataframe.drop(columns = ['tpep_pickup_datetime', 'tpep_dropoff_datetime'], inplace = True)
        
    except:
        return 'Algo salió mal al intentar separar columnas datetime.'

# %%
def nulos_amarillo(dataframe):
    '''Tratamiento de valores nulos.'''

    import numpy as np
    import pandas as pd

    #Sustituir nulos en 'congestion_surcharge' y 'airport_fee' por '0'.
    dataframe['congestion_surcharge'].fillna(value = 0, inplace = True)
    dataframe['airport_fee'].fillna(value = 0, inplace = True)

    #Promedio de 'passenger_count'.
    promedio = np.around(dataframe['passenger_count'].mean(), decimals = 0)
    #Sustituir el promedio en los valores nulos.
    dataframe['passenger_count'].fillna(promedio, inplace = True)

    #Calcular medias.
    media_distance = np.around(dataframe['trip_distance'].mean(), decimals = 0)
    media_fare = np.around(dataframe['fare_amount'].mean(), decimals = 0)
    media_tip = np.around(dataframe['tip_amount'].mean(), decimals = 0)
    media_tolls = np.around(dataframe['tolls_amount'].mean(), decimals = 0)
    media_i_s = np.around(dataframe['improvement_surcharge'].mean(), decimals = 0)

    #Sustituir nulos por medias.
    dataframe['trip_distance'].fillna(value = media_distance, inplace = True)
    dataframe['fare_amount'].fillna(value = media_fare, inplace = True)
    dataframe['tip_amount'].fillna(value = media_tip, inplace = True)
    dataframe['tolls_amount'].fillna(value = media_tolls, inplace = True)
    dataframe['improvement_surcharge'].fillna(value = media_i_s, inplace = True)

    #Calcular modas.
    moda_payment = dataframe['payment_type'].mode().astype(int)
    moda_extra = dataframe['extra'].mode().astype(int)
    moda_tax = dataframe['mta_tax'].mode().astype(int)

    #Sustituir nulos por modas.
    dataframe['payment_type'].fillna(value = moda_payment.values[0], inplace = True)
    dataframe['extra'].fillna(value = moda_extra.values[0], inplace = True)
    dataframe['mta_tax'].fillna(value = moda_tax.values[0], inplace = True)


# %% [markdown]
# ### Verdes

# %%
def columnas_verdes(dataframe):
    '''Eliminar columnas indeseadas.'''

    import numpy as np
    import pandas as pd

    try:
        dataframe.drop(columns = ['VendorID', 'store_and_fwd_flag', 'RatecodeID', 'ehail_fee', 'trip_type'], inplace = True)
        print('Se eliminaron las columnas: VendorID, store_and_fwd_flag, RatecodeID, ehail_fee')

    except:
        return 'Algo salió mal al intentar eliminar columnas.'

# %%
def dt_verdes(dataframe):
    '''Separar columnas datetime en día y hora.'''

    import numpy as np
    import pandas as pd

    try:
        #Insertar 'pickup_day'.
        dataframe.insert(0, 'pickup_day', dataframe['lpep_pickup_datetime'].dt.date)
        #Insertar 'pickup_time'.
        dataframe.insert(1, 'pickup_time', dataframe['lpep_pickup_datetime'].dt.time)
        #Insertar 'dropoff_day'.
        dataframe.insert(2, 'dropoff_day', dataframe['lpep_dropoff_datetime'].dt.date)
        #Insertar 'dropoff_time'.
        dataframe.insert(3, 'dropoff_time', dataframe['lpep_dropoff_datetime'].dt.time)
        #Eliminar 'lpep_pickup_datetime' y 'lpep_dropoff_datetime'.
        dataframe.drop(columns = ['lpep_pickup_datetime', 'lpep_dropoff_datetime'], inplace = True)

    except:
        return 'Algo salió mal al separar las columnas datetime.'

# %%
def nulos_verdes(dataframe):
    '''Tratamiento de valores nulos.'''

    import numpy as np
    import pandas as pd
    try:
        #Sustituir nulos en 'congestion_surcharge' por '0'.
        dataframe['congestion_surcharge'].fillna(value = 0, inplace = True)

        #Promedio de 'passenger_count'.
        promedio = np.around(dataframe['passenger_count'].mean(), decimals = 0)
        #Sustituir el promedio en los valores nulos de 'passenger_count'.
        dataframe['passenger_count'].fillna(promedio, inplace = True)

        #Moda de 'payment_type' y 'trip_type'.
        moda_payment = dataframe['payment_type'].mode(axis = 'columns', numeric_only = True).astype(int)
        moda_trip = dataframe['trip_type'].mode(axis = 'columns', numeric_only = True).astype(int)
        #Sustituir la moda en los valores nulos.
        dataframe['payment_type'].fillna(value = moda_payment.values[0], inplace = True)
        dataframe['trip_type'].fillna(value = moda_trip.values[0], inplace = True)

        #Calcular medias.
        media_distance = np.around(dataframe['trip_distance'].mean(), decimals = 0)
        media_fare = np.around(dataframe['fare_amount'].mean(), decimals = 0)
        media_tip = np.around(dataframe['tip_amount'].mean(), decimals = 0)
        media_tolls = np.around(dataframe['tolls_amount'].mean(), decimals = 0)
        media_i_s = np.around(dataframe['improvement_surcharge'].mean(), decimals = 0)

        #Sustituir nulos por medias.
        dataframe['trip_distance'].fillna(value = media_distance, inplace = True)
        dataframe['fare_amount'].fillna(value = media_fare, inplace = True)
        dataframe['tip_amount'].fillna(value = media_tip, inplace = True)
        dataframe['tolls_amount'].fillna(value = media_tolls, inplace = True)
        dataframe['improvement_surcharge'].fillna(value = media_i_s, inplace = True)

        #Calcular modas.
        moda_extra = dataframe['extra'].mode().astype(int)
        moda_tax = dataframe['mta_tax'].mode().astype(int)

        #Sustituir nulos por modas.
        dataframe['extra'].fillna(value = moda_extra, inplace = True)
        dataframe['mta_tax'].fillna(value = moda_tax, inplace = True)

    except:
        return 'Algo salió mal al tratar valores nulos.'

# %% [markdown]
# ### FHV

# %%
def columnas_fhv(dataframe):
    '''Eliminar columnas indeseadas.'''

    import numpy as np
    import pandas as pd
    try:
        dataframe.drop(columns = ['hvfhs_license_num', 'dispatching_base_num', 'originating_base_num', 'request_datetime', 'on_scene_datetime', 'shared_request_flag', 'shared_match_flag', 'access_a_ride_flag', 'wav_request_flag', 'wav_match_flag'], inplace = True)
        print('Se eliminaron las columnas: hvfhs_license_num, dispatching_base_num, originating_base_num, request_datetime, on_scene_datetime, shared_request_flag, shared_match_flag, access_a_ride_flag, wav_request_flag, wav_match_flag')

    except:
        return 'Algo salió mal al intentar eliminar columnas.'

# %%
def dt_fhv(dataframe):
    '''Separar columnas datetime en día y hora.'''

    import numpy as np
    import pandas as pd
    try:
        #Insertar 'pickup_day'.
        dataframe.insert(0, 'pickup_day', dataframe['pickup_datetime'].dt.date)
        #Insertar 'pickup_time'.
        dataframe.insert(1, 'pickup_time', dataframe['pickup_datetime'].dt.time)
        #Insertar 'dropoff_day'.
        dataframe.insert(2, 'dropoff_day', dataframe['dropoff_datetime'].dt.date)
        #Insertar 'dropoff_time'.
        dataframe.insert(3, 'dropoff_time', dataframe['dropoff_datetime'].dt.time)
        #Eliminar 'pickup_datetime' y 'dropoff_datetime'.
        dataframe.drop(columns = ['pickup_datetime', 'dropoff_datetime'], inplace = True)

    except:
        return 'Algo salió mal al separar las columnas datetime.'

# %%
def nulos_fhv(dataframe):
    '''Tratamiento de valores nulos.'''
    
    import numpy as np
    import pandas as pd

    try:
        #Sustituir nulos por '0'.
        dataframe['bcf'].fillna(value = 0, inplace = True)
        dataframe['congestion_surcharge'].fillna(value = 0, inplace = True)
        dataframe['airport_fee'].fillna(value = 0, inplace = True)
        dataframe['tips'].fillna(value = 0, inplace = True)

        #Calcular medias.
        media_miles = np.around(dataframe['trip_miles'].mean(), decimals = 0)
        media_time = np.around(dataframe['trip_time'].mean(), decimals = 0)
        media_fare = np.around(dataframe['base_passenger_fare'].mean(), decimals = 0)
        media_tolls = np.around(dataframe['tolls'].mean(), decimals = 0)
        media_tax = np.around(dataframe['sales_tax'].mean(), decimals = 0)
        media_driver_pay = np.around(dataframe['driver_pay'].mean(), decimals = 0)
        
        #Sustituir nulos por medias.
        dataframe['trip_miles'].fillna(value = media_miles, inplace = True)
        dataframe['trip_time'].fillna(value = media_time, inplace = True)
        dataframe['base_passenger_fare'].fillna(value = media_fare, inplace = True)
        dataframe['tolls'].fillna(value = media_tolls, inplace = True)
        dataframe['sales_tax'].fillna(value = media_tax, inplace = True)
        dataframe['driver_pay'].fillna(value = media_driver_pay, inplace = True)

    except:
        return 'Algo salió mal al tratar valores nulos.'