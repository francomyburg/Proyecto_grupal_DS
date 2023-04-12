Data Dictionary
================

|      Table      |         Field       | Data Type |                                            Description                                            |
|-----------------|---------------------|-----------|---------------------------------------------------------------------------------------------------|
|yellow           |pickup_day           |datetime64 |Date when the taximeter was engaged.                                                               |
|yellow           |pickup_time          |datetime64 |Time when the taximeter was engaged.                                                               |
|yellow           |dropoff_day          |datetime64 |Date when the taximeter was disengaged.                                                            |
|yellow           |dropoff_time         |datetime64 |Time when the taximeter was disengaged.                                                            |
|yellow           |trip_distance        |float64    |Elapsed trip distance in miles reported by the taximeter.                                          |
|yellow           |PULocationID         |int64      |TLC Taxi Zone in which the taximeter was engaged.                                                  |
|yellow           |DOLocationID         |int64      |TLC Taxi Zone in which the taximeter was disengaged.                                               |
|yellow           |payment_type         |int64      |Numeric code signifying how the passenger paid for the trip.                                       |
|yellow           |fare_amount          |float64    |The time-and-distance fare calculated by the meter.                                                |
|yellow           |tip_amount           |float64    |Tip amount. This field is automatically populated for credit card tips. Cash tips are not included.|
|yellow           |tolls_amount         |float64    |Total amount of all tolls paid in trip.                                                            |
|yellow           |total_amount         |float64    |Total amount charged to passengers. Does not include cash tips.                                    |
|yellow           |congestion_surcharge |float64    |Amount collected in trip for NYS congestion surcharge.                                             |
|yellow           |airport_fee          |float64    |$1.25 for pickup only at LaGuardia and John F. Kennedy Airports.                                   |
|green            |pickup_day           |datetime64 |Date when the taximeter was engaged.                                                               |
|green            |pickup_time          |datetime64 |Time when the taximeter was engaged.                                                               |
|green            |dropoff_day          |datetime64 |Date when the taximeter was disengaged.                                                            |
|green            |dropoff_time         |datetime64 |Time when the taximeter was disengaged.                                                            |
|green            |trip_distance        |float64    |Elapsed trip distance in miles reported by the taximeter.                                          |
|green            |PULocationID         |int64      |TLC Taxi Zone in which the taximeter was engaged.                                                  |
|green            |DOLocationID         |int64      |TLC Taxi Zone in which the taximeter was disengaged.                                               |
|green            |payment_type         |int64      |Numeric code signifying how the passenger paid for the trip.                                       |
|green            |fare_amount          |float64    |The time-and-distance fare calculated by the meter.                                                |
|green            |tip_amount           |float64    |Tip amount. This field is automatically populated for credit card tips. Cash tips are not included.|
|green            |tolls_amount         |float64    |Total amount of all tolls paid in trip.                                                            |
|green            |total_amount         |float64    |Total amount charged to passengers. Does not include cash tips.                                    |
|green            |congestion_surcharge |float64    |Amount collected in trip for NYS congestion surcharge.                                             |
|fhv              |pickup_day           |datetime64 |Date of the trip pick-up.                                                                          |
|fhv              |pickup_time          |datetime64 |Time of the trip pick-up.                                                                          |
|fhv              |dropoff_day          |datetime64 |Date of the trip drop-off.                                                                         |
|fhv              |dropoff_time         |datetime64 |Time of the trip drop-off.                                                                         |
|fhv              |trip_miles           |float64    |Total miles for passenger trip.                                                                    |
|fhv              |PULocationID         |int64      |TLC Taxi Zone in which the trip began.                                                             |
|fhv              |DOLocationID         |int64      |TLC Taxi Zone in which the trip ended.                                                             |
|fhv              |trip_time            |int64      |Total time in seconds for passenger trip.                                                          |
|fhv              |base_passenger_fare  |float64    |Base passenger fare before tolls, tips, taxes and fees.                                            |
|fhv              |tolls                |float64    |Total amount of all tolls paid in trip.                                                            |
|fhv              |tips                 |float64    |Total amount of tips received from passenger.                                                      |
|fhv              |total_amount         |float64    |Total amount charged to passengers.                                                                |
|fhv              |congestion_surcharge |float64    |Amount collected in trip for NYS congestion surcharge.                                             |
|fhv              |airport_fee          |float64    |$2.50 for both drop-off and pick-up at LaGuardia, Newark, and John F. Kennedy Airports.            |
|taxi_zone_lookup |LocationID           |int64      |TLC Taxi Zone ID.                                                                                  |
|taxi_zone_lookup |Borough              |string     |One of the five administrative units of New York City.                                             |
|taxi_zone_lookup |Zone                 |string     |Area section inside a Borough                                                                      |
|taxi_zone_lookup |service_zone         |string     |TLC Taxi service zone.                                                                             |
