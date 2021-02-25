#!/bin/python3


class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "{self.path}".format(self=self)


if __name__ == "__main__":
    streets = [
        Street(0, 1, "Main Road", 2),
        Street(1, 2, "Lewis Road", 3),
        Street(2, 3, "Marija Road", 4),
        Street(2, 3, "Mat Road", 5),
    ]
    car = Car(Path(streets))
    print(car)
