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
    

