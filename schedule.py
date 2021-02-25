from street import Street
from intersection import Intersection

class Schedule:
    
    def __init__(self, intersection, street_schedules):
        """Initialise schedule object for an intersection

        Args:
            intersection (Intersection): The intersection the schedule is controlling
            street_schedules (List of tuples (street, time_green)): Ordered list of tuples describing each street and how long it is green  
        """
        self.intersection = intersection
        self.street_schedules = street_schedules

    
    def __str__(self):
        return f"<Schedule for intersection {self.intersection.id_}>"
    

    def output_format(self):
        """Returns the schedule in the file format

        Returns:
            string: String representation of the schedule to be combined into output
        """
        output = f"{self.intersection.id_}\n"
        output += f"{len(self.street_schedules)}\n"

        for schedule in self.street_schedules:
            street = schedule[0]
            time_green = schedule[1]

            output += f"{street.name} {time_green}\n"

        return output


if __name__ == "__main__":
    intersection = Intersection(0)
    intersection2 = Intersection(1)

    street = Street(0, 1, "Main Road", 5)

    schedule = Schedule(intersection, [(street, 5)])

    print(schedule.output_to_file())
