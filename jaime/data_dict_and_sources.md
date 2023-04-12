# <h1> DATA INFO </h1> 


## Data Sources

TLC Trip Record Data .<br>

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page<br>

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

## Data Dictionary

| **DATA DICTIONARY ENVIROMENTAL TABLES** 	|  	|
|:---:	|:---:	|
| **Header** 	| **Description** 	|
| _date_ 	| _data collection date_ 	|
| _id_cd_ 	| _Community District   geographical id_ 	|
| _cd_name_ 	| _Community District name_ 	|
| _id_borough_ 	| _Borough geographical id_ 	|
| _borough_ 	| _Borough name_ 	|
| _pm 2.5_ 	| _total particulate matter in the air µg/cm3_ 	|
| _air_quality_ 	| _air quality classification_ 	|
| _volume_ 	| _number of vehicles per 15 minutes_ 	|
| **DATA DICTIONARY CABS TABLES** 	|  	|
| **Header** 	| **Description** 	|
| _license_class_ 	| _Category based on the type of service offered with the   vehicle being driven._ 	|
| _trips_per_day_ 	| _Daily average of individual   rides or trips taken by passengers on a given month._ 	|
| _farebox_per_day_ 	| _Daily average amount of money   collected from passengers on a given month._ 	|
| _unique_drivers_ 	| _Average of individual drivers   who operate a vehicle within a month._ 	|
| _unique_vehicles_ 	| _Average of individual vehicles   that are operated within a month._ 	|
| _vehicles_per_day_ 	| _Daily average of vehicles that   are operated on a given month._ 	|
| _avg_days_vehicles_on_road_ 	| _Average of days that vehicles   are in operation on a given month._ 	|
| _avg_hours_per_day_per_vehicle_ 	| _Daily average of hours that a   vehicle is in operation on a given month._ 	|
| _avg_days_drivers_on_road_ 	| _Average of days that drivers are   working in a given month._ 	|
| _avg_hours_per_day_per_driver_ 	| _Daily average of hours that a   driver is working on a given month._ 	|
| _avg_minutes_per_trip_ 	| _Average length of time for a   single trip or ride taken by a passenger._ 	|
| _percent_of_trips_paid_with_credit_card_ 	| _Proportion of rides or trips   that are paid for using a credit card._ 	|
| _trips_per_day_shared_ 	| _Daily average of shared rides or   trips taken by passengers on a given month._ 	|
| _month_year1_ 	| _Month-Year_ 	|
| _trips_per_month_ 	| _Number of individual rides or   trips taken by passengers on a given month._ 	|
| _month_date_ 	| _Year-Month-Date_ 	|
| _farebox_per_month_ 	| _Total amount of money collected   from passengers on a given month._ 	|
| _week_ 	| _Number of week for a given year._ 	|
| _trips_per_week_ 	| _Number of individual rides or   trips taken by passengers on a given week._ 	|
| _year_ 	| _Number of year._ 	|
| _farebox_per_week_ 	| _Total amount of money collected   from passengers on a given week._ 	|
| _total_trips_per_day_ 	| _Daily average of individual plus   shared rides or trips taken by passengers on a given month._ 	|
| _shared_trips_per_day_percent_ 	| _Proportion of rides or trips   that are shared on daily average._ 	|


<hr>

- **Table_1: air_quality**

- **Tabla_2: vehicular_volume**
