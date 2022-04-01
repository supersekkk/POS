
def main():
    user_choice = (input("What would you like to do? \n1. Fahrenheit to Celcius\n2. Celcius to Fahrenheit"))
    if user_choice == "1":
        fahrenheit = float(input("How many fahrenheit would you like to convert?"))
        print(fahrenheit_to_celcius(fahrenheit))
    elif user_choice == "2":
        celsius = float(input("How many celcius would you like to convert?)"))
        print(celcius_to_fahrenheit(celsius))
    else:
        print("\nInvalid answer. Please try again\n")
        main()


def fahrenheit_to_celcius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

def celcius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

main()