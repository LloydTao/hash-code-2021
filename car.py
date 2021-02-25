#!/bin/python3


class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "{self.path}".format(self=self)


if __name__ == "__main__":
    streets = [
        "Main Road",
        "Lewis Road",
        "Marija Road",
        "Mat Road",
    ]
    car = Car(streets)
    print(car)
