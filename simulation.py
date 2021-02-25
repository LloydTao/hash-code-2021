class Simulation:
    def __init__(self, duration, points, streets, intersections, cars):
        self.duration = duration
        self.points = points
        self.streets = streets
        self.intersections = intersections
        self.cars = cars

        # add cars to streets
        for car in cars:
            self.get_street_by_name(car.path[0]).cars.append(car)

        self.run()

    def get_street_by_name(self, street_name):
        for street in self.streets:
            if street_name == street.name:
                return street

    def run(self):
        pass
