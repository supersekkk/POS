year_current = 2022
vintage = 50

class GuitarEntities:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{}, first made in {}, and it costs {}" .format(self.name, self.year, self.cost)

    def get_age(self):
        return year_current - self.year

    def is_vintage(self):
        return self.get_age() >= vintage

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year

