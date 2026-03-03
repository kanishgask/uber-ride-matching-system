import math

class LocationService:
    def __init__(self):
        self.driver_locations = {}  # driver_id -> (lat, lon)

    def update_location(self, driver_id, lat, lon):
        self.driver_locations[driver_id] = (lat, lon)

    def _distance(self, lat1, lon1, lat2, lon2):
        return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

    def find_nearby_drivers(self, rider_lat, rider_lon, radius=5):
        nearby = []
        for driver_id, (lat, lon) in self.driver_locations.items():
            if self._distance(rider_lat, rider_lon, lat, lon) <= radius:
                nearby.append(driver_id)
        return nearby


# Demo
if __name__ == "__main__":
    loc = LocationService()
    loc.update_location("D1", 10, 10)
    loc.update_location("D2", 15, 15)

    print(loc.find_nearby_drivers(10, 10))
