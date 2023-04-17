# <h1> ETL </h1> 


## 1. Extract

### Data Sources

TLC Trip Record Data .<br>

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page <br>

Air pollution NYC.<br>

https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r<br>
API "https://data.cityofnewyork.us/resource/c3uy-2p5r.json"

Traffic Density/Volume NYC.<br>

https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt <br>
API "https://data.cityofnewyork.us/resource/7ym2-wayt.json"

Noise pollution NYC.<br>

Registro de tipos de sonidos en NYC.<br>
https://zenodo.org/record/3966543/files/annotations.csv?download=1<br>

<hr>

## 2. Transform

Datos que relacionan los viajes que realizan los taxis amarillos en NYC. [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

| **Data_source** | **Activities** |
|---|---|
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se elimina **'VendorID', 'RatecodeID', 'store_and_fwd_flag'** |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se Separa   **'lpep_pickup_datetime' y 'lpep_dropoff_datetime'**  en día (YYYY-MM-DD) **Hora de pickup**,   **Hora de dropoff**. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   insertan las variables **'dropoff_time' 'pickup_day' 'pickup_time'   'dropoff_day'**	 |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |      Se elimina **'lpep_pickup_datetime'    'lpep_dropoff_datetime'** |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   identifican valores faltantes nan en **'passenger_count'**: 22188   **'congestion_surcharge'**:8195675 **'airport_fee'**: 8195675. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   imputa == 0 a las variables **'congestion_surcharge' 'airport_fee'** con   valores faltantes nan. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   imputa valores de la media a las variables **'trip_distance' 'fare_amount'   'tip_amount' 'passenger_count' 'tolls_amount' 'improvement_surcharge'** con   valores faltantes nan. |
| [TLC Trip Record   Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | Se   imputa valores de la moda las variables **'payment_type'** , **'trip_type'**   , **'extra'**, **'mta_tax'** con valores faltantes nan. |

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

Se generan 6 tablas.<br>


<hr>

## 3. Load

### Carga de tablas de aspectos ambientales

### Carga de tabla de viajes de taxis
Se emplea el siguiente scrip para la carga de todos los viajes realizados por los taxis amarillos en NYC. <br>


*Developed by*

<a href="https://www.linkedin.com/in/franco-jonas-myburg-6095b8255/"><img alt="Franco" title="Connect with Franco" src="https://img.shields.io/badge/Franco Myburg-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/ivannagvdc/"><img alt="Ivanna" title="Connect with Ivanna" src="https://img.shields.io/badge/Ivanna Villa-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ANALYST**

<a href="https://www.linkedin.com/in/jospinoponce/"><img alt="Jaime" title="Connect with Jaime" src="https://img.shields.io/badge/Jaime Ospino-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**

<a href="https://www.linkedin.com/in/takticflow/"><img alt="Luciano" title="Connect with Luciano" src="https://img.shields.io/badge/Luciano Larrea-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **PROJECT MANAGER & DATA SCIENTIST**

<a href="https://www.linkedin.com/in/royquillca/"><img alt="Roy" title="Connect with Roy" src="https://img.shields.io/badge/Roy Quillca-0077B5?style=flat&logo=Linkedin&logoColor=white"></a> **DATA ENGINEER**




