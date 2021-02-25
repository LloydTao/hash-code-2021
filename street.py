#!/bin/python3

from intersection import Intersection


class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length

    def __str__(self):
        return "{self.name} (Len: {self.length}) | {self.start} -> {self.end}".format(
            self=self
        )


if __name__ == "__main__":
    start = Intersection(0)
    end = Intersection(1)
    street = Street(start, end, "Main Road", 5)
    print(street)
