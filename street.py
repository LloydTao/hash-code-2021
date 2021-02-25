from car import Car
from intersection import Intersection


class Street:
    def __init__(self, start, end, name, length, cars):
        self.start = start
        self.end = end
        self.name = name
        self.length = length
        self.cars = cars

    def get_cars(self):
        """
        Returns the list of cars.
        """
        return self.cars

    def get_car(self, i):
        """
        Returns the car at position i.
        """
        return self.cars[i]

    def add_car(self, car):
        """
        Add a car to the end of the queue.
        Returns the list of cars.
        """
        return self.cars.append(car)

    def remove_car(self):
        """
        Remove a car from the front of the queue.
        Returns the popped car.
        """
        return self.cars.pop()

    def __str__(self):
        return "{self.name} (Len: {self.length}) | {self.start} -> {self.end}".format(
            self=self
        )


if __name__ == "__main__":

    # Test Street
    start = Intersection(0)
    end = Intersection(1)
    street = Street(start, end, "First Road", 5, [])
    print(street, "\n")

    # Test Cars on Street
    streets = ["Main Road", "Lewis Road"]
    cars = [Car(streets), Car(streets)]
    street = Street(start, end, "First Road", 5, cars)
    print("First car:", street.get_car(0), "\n")
    print("Second car:", street.get_car(1), "\n")
    print("Two cars:", street.get_cars(), "\n")

    # Test removing Car from Street
    street.remove_car()
    print("One cars:", street.get_cars(), "\n")

    # Test adding Car to Street
    street.add_car(Car(streets))
    print("Two cars:", street.get_cars(), "\n")
