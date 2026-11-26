class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name
        self.vehicle_plate = vehicle_plate
        self.__rating = 5.0
        self.__total_trips = 0

    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid rating!")

        self.__rating = ((self.__rating * self.__total_trips + new_rating)/ (self.__total_trips + 1))

        self.__total_trips += 1

    def get_rating_info(self):
        return (f"Driver: {self.name}, "f"Average Rating: {self.__rating:.2f}, "f"Total Trips: {self.__total_trips}")