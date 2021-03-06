import math
import os
import random
import re
import sys

import numpy as np
import street
from intersection import Intersection
from car import Car
from street import Street


def populate_objects(dataset_path):
    """
    Read input datatset and populate Street, Intersection and Car objects.
    """

    intersections = []
    streets = []
    cars = []

    with open(dataset_path) as f:

        data = [line.strip().split(" ") for line in f.readlines()]
        data[0] = list(map(int, data[0]))
        dur, inter, street_idx, paths, points = (
            data[0][0],
            data[0][1],
            data[0][2],
            data[0][3],
            data[0][4],
        )

        intersections = [Intersection(i) for i in range(inter)]
        streets = [
            Street(intersections[int(i[0])], intersections[int(i[1])], i[2], i[3])
            for i in data[1 : street_idx + 1]
        ]

        paths = [i[1:] for i in data[street_idx + 1 :]]
        cars = [Car(path) for path in paths]

    return dur, intersections, streets, cars, points


class Solution:
    def solve_stuff(self, a, b, c, n):
        pass


if __name__ == "__main__":
    duration, intersections, streets, cars, points = populate_objects("input/a.txt")
