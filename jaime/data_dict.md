# <h1> DATA DICTIONARY </h1> 


## Data Dictionary
<br>

| **DATA   DICTIONARY CABS TABLES** |   |
|---|:---:|
| **Table_0:taxi+_zone_lookup.csv** | ** ** |
| **Header** | **Description** |
| _borough_name_ | _new york district name_ |
| _service_zone       _ | _taxi operating area_ |
| **Table_1: TLC_Monthy_Report_NYC.csv** | ** ** |
| **Header** | **Description** |
| _license_class_ | _Category  based on the type of service offered with the vehicle being driven._ |
| _trips_per_day_ | _Daily   average of individual rides or trips taken by passengers on a given month._ |
| _farebox_per_day_ | _Daily   average amount of money collected from passengers on a given month._ |
| _unique_drivers_ | _Average   of individual drivers who operate a vehicle within a month._ |
| _unique_vehicles_ | _Average   of individual vehicles that are operated within a month._ |
| _vehicles_per_day_ | _Daily   average of vehicles that are operated on a given month._ |
| _avg_days_vehicles_on_road_ | _Average   of days that vehicles are in operation on a given month._ |
| _avg_hours_per_day_per_vehicle_ | _Daily   average of hours that a vehicle is in operation on a given month._ |
| _avg_days_drivers_on_road_ | _Average   of days that drivers are working in a given month._ |
| _avg_hours_per_day_per_driver_ | _Daily   average of hours that a driver is working on a given month._ |
| _avg_minutes_per_trip_ | _Average   length of time for a single trip or ride taken by a passenger._ |
| _percent_of_trips_paid_with_credit_card_ | _Proportion   of rides or trips that are paid for using a credit card._ |
| _trips_per_day_shared_ | _Daily   average of shared rides or trips taken by passengers on a given month._ |
| _month_year1_ | _Month-Year_ |
| _trips_per_month_ | _Number   of individual rides or trips taken by passengers on a given month._ |
| _month_date_ | _Year-Month-Date_ |
| _farebox_per_month_ | _Total   amount of money collected from passengers on a given month._ |
| _week_ | _Number   of week for a given year._ |
| _trips_per_week_ | _Number   of individual rides or trips taken by passengers on a given week._ |
| _year_ | _Number   of year._ |
| _farebox_per_week_ | _Total   amount of money collected from passengers on a given week._ |
| _total_trips_per_day_ | _Daily   average of individual plus shared rides or trips taken by passengers on a   given month._ |
| _shared_trips_per_day_percent_ | _Proportion   of rides or trips that are shared on daily average._ |
| **Table_2: yellow_cabs_NYC** |   |
| **Header** | **Description** |
| _id_vendor_ | _A code   indicating the LPEP provider that provided the record._ |
| _lpep_pickup_datetime_ | _The   date and time when the meter was engaged._ |
| _lpep_dropoff_datetime_ | _The   date and time when the meter was disengaged._ |
| _store_and_fwd_flag_ | _This   flag indicates whether the trip record was held in vehicle memory before   sending to the vendor._ |
| _id_rate_code_ | _The   final rate code in effect at the end of the trip._ |
| _pickup_longitude_ | _GPS   longitude coordinate of the pickup location._ |
| _pickup_latitude_ | _GPS   latitude coordinate of the pickup location._ |
| _dropoff_longitude_ | _GPS   longitude coordinate of the drop-off location._ |
| _dropoff_latitude_ | _GPS   latitude coordinate of the drop-off location._ |
| _passenger_count_ | _The   number of passengers in the vehicle._ |
| _trip_distance_ | _The   elapsed trip distance in miles reported by the taximeter._ |
| _fare_amount_ | _The   time-and-distance fare calculated by the meter._ |
| _extra_ | _Miscellaneous   extras and surcharges._ |
| _mta_tax_ | _$0.50   MTA tax that is automatically triggered based on the metered rate in use._ |
| _tip_amount_ | _Tip   amount – This field is automatically populated for credit card tips. Cash   tips are not included._ |
| _tolls_amount_ | _Total   amount of all tolls paid in trip._ |
| _ehail_fee_ | _$1.00   improvement surcharge assessed trips at the request of MTA_ |
| _improvement_surcharge_ | _$0.30   improvement surcharge assessed trips at the request of MTA._ |
| _total_amount_ | _The   total amount charged to passengers._ |
| _payment_type_ | _A   numeric code signifying how the passenger paid for the trip._ |
| _trip_type_ | _A code   indicating whether the trip was a street-hail or a dispatch that is   automatically assigned based on the metered rate in use but can be altered by   the driver._ |
| _id_pu_location_ | _TLC   Taxi Zone in which the taximeter was engaged_ |
| _id_do_location_ | _TLC   Taxi Zone in which the taximeter was disengaged_ |
| **DATA DICTIONARY ENVIROMENTAL TABLES** | ** ** |
| **Table_3: air_pollution.csv** | ** ** |
| **Header** | **Description** |
| _date_ | _data   collection date_ |
| _id_cd_ | _Community   District geographical id_ |
| _cd_name_ | _Community   District name_ |
| _id_borough_ | _Borough   geographical id_ |
| _borough_name_ | _Borough   name_ |
| _polluting_agent_ | _type   of pollutant in the air_ |
| _data_value_ | _amount   of pollutant in the air_ |
| **Table_4: air_quality.csv** | ** ** |
| **Header** | **Description** |
| _pm 2.5_ | _total   particulate matter in the air µg/cm3_ |
| _air_quality_ | _air   quality classification_ |
| **Table_5: vehicular_volume.csv** | ** ** |
| **Header** | **Description** |
| _volume_ | _number   of vehicles per 15 minutes_ |
| **Table_6:   noise_pollution.csv** | ** ** |
| **Header** | **Description** |
| _engine_sounds_ | _motor noise records_ |
| _alarm_sounds_ | _noise records by car alarm system_ |