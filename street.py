#!/bin/python3


class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.name = name
        self.length = length

    def __str__(self):
        return "{self.name}".format(self=self)


if __name__ == "__main__":
    street = Street(0, 1, "Main Road", 5)
    print(street)
