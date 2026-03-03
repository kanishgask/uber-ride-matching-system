class RideMatchingService:

    def __init__(self, location_service):
        self.location_service = location_service
        self.active_rides = {}

    def request_ride(self, rider_id, lat, lon):
        drivers = self.location_service.find_nearby_drivers(lat, lon)

        if not drivers:
            return "No drivers available"

        selected_driver = drivers[0]

        ride_id = f"ride_{rider_id}_{selected_driver}"
        self.active_rides[ride_id] = {
            "rider": rider_id,
            "driver": selected_driver,
            "status": "requested"
        }

        return ride_id


# Demo
if __name__ == "__main__":
    from location_service import LocationService

    loc = LocationService()
    loc.update_location("D1", 10, 10)

    matcher = RideMatchingService(loc)
    ride = matcher.request_ride("R1", 10, 10)
    print(ride)
