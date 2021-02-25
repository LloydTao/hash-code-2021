class Intersection:
    def __init__(self, id_, schedule=[]):
        self.id_ = id_
        self.schedule = schedule

    def __str__(self):
        return f"<Intersection {self.id_}>"


if __name__ == "__main__":
    intersection = Intersection(0)
    print(intersection)
