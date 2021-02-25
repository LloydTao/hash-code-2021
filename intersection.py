class Intersection:
    def __init__(self, id_):
        self.id_ = id_

    def __str__(self):
        return f"<Intersection {self.id_}>"


if __name__ == "__main__":
    intersection = Intersection(0)
    print(intersection)
