# 📊 ER Diagram - Ride Matching

USERS
- user_id (PK)
- role (rider/driver)
- rating

RIDES
- ride_id (PK)
- rider_id (FK)
- driver_id (FK)
- status
- pickup_lat
- pickup_lon

DRIVER_LOCATIONS
- driver_id (PK, FK)
- latitude
- longitude

Relationships:

User (rider) 1 → N Rides  
User (driver) 1 → N Rides  
Driver 1 → 1 Current Location
