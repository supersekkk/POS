
from prac_06.guitar_entities import GuitarEntities

def run_test():
    name = "Bison L-5"
    year = 1977
    cost = 16035.40

    guitar = GuitarEntities(name, year, cost)
    other = GuitarEntities("Other guitar", 2013, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))


if __name__ == '__main__':
    run_test()