# <h1> ETL </h1> 

Se realizan procesos de extracción y transformación a datos que tienen información de la ciudad de New York y de los viajes realizados por taxis en sus diferentes distritos para cargarlos en una base de datos en la nube de Microsoft Azure. 

Los scripts necesarios para el desarrollo de las actividades puede ser consultado en: []

## 1. Extract

### Data Sources

**Datos de viajes de los taxis en NYC:**<br>

Se realiza la extracción con python y se almacenan los datos en Azure Blob Storage.<br>

TLC Trip Record Data .<br>
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page <br>


**Datos del medio ambiente NYC:**<br>

Se realiza la extracción de los datos y se almacena de manera local: [data_finale](https://github.com/francomyburg/Proyecto_grupal_DS/tree/main/data/finale_dataset).

Air pollution NYC.<br>
https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r<br>
API "https://data.cityofnewyork.us/resource/c3uy-2p5r.json"

Traffic Density/Volume NYC.<br>
https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt <br>
API "https://data.cityofnewyork.us/resource/7ym2-wayt.json"

Noise pollution NYC.<br>
Registro de tipos de sonidos en NYC https://zenodo.org/record/3966543/files/annotations.csv?download=1<br>

<hr>

## 2. Transform

Datos que relacionan los viajes que realizan los taxis amarillos en NYC. [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

| **Data_source** | **Activities** |
|---|---|
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se elimina **'VendorID', 'RatecodeID', 'store_and_fwd_flag'** |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   identifican valores faltantes nan en **'passenger_count'**: 22188   **'congestion_surcharge'**:8195675 **'airport_fee'**: 8195675. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   imputa == 0 a las variables **'fare_amount'** **'extra'** **'mta_tax'** **'tolls_amount'** **'congestion_surcharge'** **'improvement_surcharge'** **'airport_fee'** con   valores faltantes nan. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se aplica valor absoluto a todas las columnas con tipo de dato numérico (para contrarrestar valores negativos, cuyo valor absoluto es congruente).|
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se eliminan filas con ubicación desconocida (valores 264 y 265) en **'PULocationID'** y **'DOLocationID'**.|
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se eliminan filas con años no correspondientes al de la tabla actual en columna **'tpep_pickup_datetime'**.|

Datos del medio ambiente.<br>

| **Data_source** | **Activities** |
|---|---|
| [Air pollution   NYC](     https://data.cityofnewyork.us/resource/c3uy-2p5r.json) | Se   modifica la fecha en **'start_date'** a (YYYY-MM-DD) |
| [Air pollution   NYC](     https://data.cityofnewyork.us/resource/c3uy-2p5r.json) | Se   eliminan columnas **'unique_id', 'indicator_id',   'measure','geo_type_name','time_period', 'measure_info'** |
| [Air pollution   NYC](     https://data.cityofnewyork.us/resource/c3uy-2p5r.json) | Se   renombran categorías de la columna **'name'** |
| [Air pollution   NYC](     https://data.cityofnewyork.us/resource/c3uy-2p5r.json) | Se   crea columna nueva **'borough_name', 'id_borough'** |
| [Traffic   Density/Volume   NYC](https://data.cityofnewyork.us/resource/7ym2-wayt.json) | Se   renombran columnas **'Yr', 'M','D', 'Boro','date','Vol'** |
| [Traffic   Density/Volume   NYC](https://data.cityofnewyork.us/resource/7ym2-wayt.json) | Se   crea columna **'date',   'borough_name'** |
| [Noise   pollution NYC](      https://zenodo.org/record/3966543/files/annotations.csv?download=1) | Se reemplaza -1 por 1 en todo el   dataset |
| [Noise   pollution NYC](      https://zenodo.org/record/3966543/files/annotations.csv?download=1) | Se seleccionan del dataset las   columnas **['1-1_small-sounding-engine_presence',  '1-2_medium-sounding-engine_presence',  '1-3_large-sounding-engine_presence',   '1-X_engine-of-uncertain-size_presence'] y   [ '5-1_car-horn_presence', '5-2_car-alarm_presence',   '5-3_siren_presence',     '5-4_reverse-beeper_presence', '5-X_other-unknown-alert-signal_presence',   '6-1_stationary-music_proximity']** |
| [Noise   pollution NYC](      https://zenodo.org/record/3966543/files/annotations.csv?download=1) | se generan la columnas   **'engine_sounds' y 'alarm_sounds'** |
| [Noise   pollution NYC](      https://zenodo.org/record/3966543/files/annotations.csv?download=1) | se renombras columnas |
| [Noise   pollution NYC](      https://zenodo.org/record/3966543/files/annotations.csv?download=1) | se selecciona **['borough',   'year', 'week', 'day', 'hour', 'engine_sounds', 'alarm_sounds']** |

Se generan 5 tablas.<br>

| **table** | **name** |
|:---:|:---:|
| table_0 | _TLC_Monthy_Report_NYC.csv_ |
| table_1 | _tlc_yellow_cabs.parquet_ |
| table_3 | _air_pollution.csv_ |
| table_4 | _vehicular_volume.csv_ |
| table_5 | _noise_pollution.csv_ |

<hr>

## 3. Load

### Carga de tablas de aspectos ambientales

### Carga de tabla de viajes de taxis

Se emplea Azure Databricks para realizar la carga:<br>

[Video de Automatización](https://www.youtube.com/watch?v=4nu3QpO49Kw)

1. Auto Loader se integró para procesar incrementalmente los nuevos archivos que se descargan a Azure Blob Storage. 

2. Esta función se encarga de validar los datos, de forma que sólo acepte valores nulos en las columnas especificadas y que la estructura del archivo se apegue al esquema indicado.

3. Los archivos se procesan automáticamente una vez el trabajo se calendariza en la sección Compute de Databricks.

4. Se utilizó PySpark para algunas modificaciones antes de la carga final de las tablas, que son "Streaming Tables" y se transforman a un formato adecuado para Azure SQL Database.

 <br>

<hr>
*Developed by*

<a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**




