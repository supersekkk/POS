from prac_06.guitar_entities import GuitarEntities

def main():
    guitars = []

    name = input("What is the name of the guitar?")
    while name != "":
        year = int(input("From year?"))
        cost = int(input("What was the cost?"))
        add_guitar = GuitarEntities(name, year, cost)
        guitars.append(add_guitar)
        print("Added ", add_guitar)
        name = input(input("Guitar name:"))

        guitars.append(GuitarEntities("Gibson L-5 CES", 1922, 16035.40))
        guitars.append(GuitarEntities("Line 6 JTV-59", 2010, 1512.9))

        if guitars:
            guitars.sort()
            print("These are my guitars:")
            for i, guitar in enumerate(guitars):
                print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(i+1, guitar.name, guitar.year, guitar.cost))
        else:
            print("No guitars :( Quick, go and buy one!")
main()
