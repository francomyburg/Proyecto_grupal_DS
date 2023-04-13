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
| **DATA   DICTIONARY CABS TABLES** |  |
|---|---|
| **Table_1:   TLC_Monthy_Report_NYC.csv** |  |
| **Header** | **Description** |
| _license_class_ | _Category based on the type of service offered with the vehicle being   driven._ |
| _trips_per_day_ | _Daily average of individual rides or trips taken by passengers on a given   month._ |
| _farebox_per_day_ | _Daily average amount of money collected from passengers on a given month._ |
| _unique_drivers_ | _Average of individual drivers who operate a vehicle within a month._ |
| _unique_vehicles_ | _Average of individual vehicles that are operated within a month._ |
| _vehicles_per_day_ | _Daily average of vehicles that are operated on a given month._ |
| _avg_days_vehicles_on_road_ | _Average of days that vehicles are in operation on a given month._ |
| _avg_hours_per_day_per_vehicle_ | _Daily average of hours that a vehicle is in operation on a given month._ |
| _avg_days_drivers_on_road_ | _Average of days that drivers are working in a given month._ |
| _avg_hours_per_day_per_driver_ | _Daily average of hours that a driver is working on a given month._ |
| _avg_minutes_per_trip_ | _Average length of time for a single trip or ride taken by a passenger._ |
| _percent_of_trips_paid_with_credit_card_ | _Proportion of rides or trips that are paid for using a credit card._ |
| _trips_per_day_shared_ | _Daily average of shared rides or trips taken by passengers on a given   month._ |
| _month_year1_ | _Month-Year_ |
| _trips_per_month_ | _Number of individual rides or trips taken by passengers on a given month._ |
| _month_date_ | _Year-Month-Date_ |
| _farebox_per_month_ | _Total amount of money collected from passengers on a given month._ |
| _week_ | _Number of week for a given year._ |
| _trips_per_week_ | _Number of individual rides or trips taken by passengers on a given week._ |
| _year_ | _Number of year._ |
| _farebox_per_week_ | _Total amount of money collected from passengers on a given week._ |
| _total_trips_per_day_ | _Daily average of individual plus shared rides or trips taken by   passengers on a given month._ |
| _shared_trips_per_day_percent_ | _Proportion of rides or trips that are shared on daily average._ |
| **Table_2: yellow_cabs_NYC** |  |
| **Header** | **Description** |
| _VendorID_ | _A code indicating the LPEP   provider that provided the record._ |
| _lpep_pickup_datetime_ | _The date and time when the meter   was engaged._ |
| _lpep_dropoff_datetime_ | _The date and time when the meter   was disengaged._ |
| _store_and_fwd_flag_ | _This flag indicates whether the   trip record was held in vehicle memory before sending to the vendor._ |
| _RateCodeID_ | _The final rate code in effect at   the end of the trip._ |
| _Pickup_longitude_ | _GPS longitude coordinate of the   pickup location._ |
| _Pickup_latitude_ | _GPS latitude coordinate of the   pickup location._ |
| _Dropoff_longitude_ | _GPS longitude coordinate of the   drop-off location._ |
| _Dropoff_latitude_ | _GPS latitude coordinate of the   drop-off location._ |
| _Passenger_count_ | _The number of passengers in the   vehicle._ |
| _Trip_distance_ | _The elapsed trip distance in   miles reported by the taximeter._ |
| _Fare_amount_ | _The time-and-distance fare   calculated by the meter._ |
| _Extra_ | _Miscellaneous extras and   surcharges._ |
| _MTA_tax_ | _$0.50 MTA tax that is   automatically triggered based on the metered rate in use._ |
| _Tip_amount_ | _Tip amount – This field is   automatically populated for credit card tips. Cash tips are not included._ |
| _Tolls_amount_ | _Total amount of all tolls paid   in trip._ |
| _Ehail_fee_ | _$1.00 improvement surcharge   assessed trips at the request of MTA_ |
| _improvement_surcharge_ | _$0.30 improvement surcharge   assessed trips at the request of MTA._ |
| _Total_amount_ | _The total amount charged to   passengers._ |
| _Payment_type_ | _A numeric code signifying how   the passenger paid for the trip._ |
| _Trip_type_ | _A code indicating whether the   trip was a street-hail or a dispatch that is automatically assigned based on   the metered rate in use but can be altered by the driver._ |
| _PULocationID_ | _TLC Taxi Zone in which the   taximeter was engaged_ |
| _DOLocationID_ | _TLC Taxi Zone in which the   taximeter was disengaged_ |
| **Table_3: green_cabs_NYC** |  |
| **Header** | **Description** |
| _VendorID_ | _A code indicating the TPEP   provider that provided the record. 1= Creative Mobile Technologies, LLC; 2=   VeriFone Inc._ |
| _passenger_count_ | _The number of passengers in the   vehicle. This is a driver-entered value._ |
| _trip_distance_ | _The elapsed trip distance in   miles reported by the taximeter._ |
| _RatecodeID_ | _The final rate code in effect at   the end of the trip. 1= Standard rate, 2=JFK, 3=Newark, 4=Nassau or   Westchester, 5=Negotiated fare, 6=Group ride_ |
| _store_and_fwd_flag_ | _This flag indicates whether the   trip record was held in vehicle memory before sending to the vendor._ |
| _PULocationID_ | _TLC Taxi Zone in which the   taximeter was engaged_ |
| _DOLocationID_ | _TLC Taxi Zone in which the   taximeter was disengaged_ |
| _payment_type_ | _A numeric code signifying how   the passenger paid for the trip. 1= Credit card, 2= Cash, 3= No charge, 4=   Dispute, 5= Unknown, 6= Voided trip_ |
| _fare_amount_ | _The time-and-distance fare   calculated by the meter._ |
| _extra_ | _Miscellaneous extras and   surcharges. Currently, this only includes the 0.50 and 1 rush hour and   overnight charges._ |
| _mta_tax_ | _$0.50 MTA tax that is   automatically triggered based on the metered rate in use._ |
| _tip_amount_ | _This field is automatically   populated for credit card tips. Cash tips are not included._ |
| _tolls_amount_ | _Total amount of all tolls paid   in trip._ |
| _improvement_surcharge_ | _$0.30 improvement surcharge   assessed on hailed trips at the flag drop. The improvement surcharge began   being levied in 2015._ |
| _total_amount_ | _The total amount charged to   passengers. Does not include cash tips._ |
| **Table_4: FHV_cabs_NYC** |  |
| **Header** | **Description** |
| _hvfhs_license_num_ | _TLC License number of the HVFHS   base or business: HV0002 Juno, HV0003 Uber, HV0004 Via, HV0005 Lyft._ |
| _dispatching_base_num_ | _TLC Base License Number of the   base that dispatched the trip._ |
| _dropoff_datetime_ | _The date and time of the trip   drop-off._ |
| _PULocationID_ | _TLC Taxi Zone in which the trip   began._ |
| _DOLocationID_ | _TLC Taxi Zone in which the trip   ended._ |
| _originating_base_num_ | _Base number of the base that   received the original trip request._ |
| _request_datetime_ | _Date/time when passenger   requested to be picked up._ |
| _trip_miles_ | _Total miles for passenger trip._ |
| _trip_time_ | _Total time in seconds for   passenger trip._ |
| _base_passenger_fare_ | _Base passenger fare before   tolls, tips, taxes, and fees._ |
| _tolls_ | _Total amount of all tolls paid   in trip._ |
| _bcf_ | _Total amount collected in trip   for Black Car Fund._ |
| _sales_tax_ | _Total amount collected in trip   for NYS sales tax._ |
| _congestion_surcharge_ | _Total amount collected in trip   for NYS congestion surcharge._ |
| _airport_fee_ | _$2.50 for both drop off and pick   up at LaGuardia, Newark, and John F. Kennedy airports._ |
| _tips_ | _Total amount of tips received   from passenger._ |
| _driver_pay_ | _Total driver pay (not including   tolls or tips and net of commission, surcharges, or taxes)._ |
| _shared_request_flag_ | _Did the passenger agree to a   shared/pooled ride, regardless of whether they were matched? (Y/N)_ |
| _shared_match_flag_ | _Did the passenger share the   vehicle with another passenger who booked separately at any point during the   trip? (Y/N)_ |
| _wav_request_flag_ | _Did the passenger request a   wheelchair-accessible vehicle (WAV)? (Y/N)_ |
| _wav_match_flag_ | _Did the trip occur in a   wheelchair-accessible vehicle (WAV)? (Y/N)_ |
| _access_a_ride_flag_ | _Was the trip administered on   behalf of the Metropolitan Transportation Authority (MTA)? (Y/N)_ |
| **Table_5: FHVHV_cabs_NYC** |  |
| **Header** | **Description** |
| _Dispatching_base_num_ | _TLC base license number of base that dispatched the FHVs_ |
| _Pickup_date_ | _Date   and time when the vehicle was dispatched, rounded to the nearest half hour_ |
| _Affiliated_base_num_ | _TLC base license number of the base that the affiliated FHV driver is   affiliated with_ |
| _locationID_ | _Location ID where the FHV picked up the passenger(s)_ |
| **DATA DICTIONARY ENVIROMENTAL   TABLES** |  |
| **Table_6: air_pollution.csv** |  |
| **Header** | **Description** |
| _date_ | _data   collection date_ |
| _id_cd_ | _Community   District geographical id_ |
| _cd_name_ | _Community   District name_ |
| _id_borough_ | _Borough   geographical id_ |
| _borough_ | _Borough   name_ |
| _polluting_agent_ | _type of pollutant in the air_ |
| _data_value_ | _amount of pollutant in the air_ |
| **Table_7: air_quality.csv** |  |
| **Header** | **Description** |
| _pm 2.5_ | _total   particulate matter in the air µg/cm3_ |
| _air_quality_ | _air   quality classification_ |
| **Table_8: vehicular_volume.csv** |  |
| **Header** | **Description** |
| _volume_ | _number   of vehicles per 15 minutes_ |