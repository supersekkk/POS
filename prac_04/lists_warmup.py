numbers = [3, 1, 4, 1, 5, 9, 2]

#    numbers[0] = 3
#    numbers[-1] = 2
#    numbers[3] = 1
#    numbers[:-1] - 3, 1, 4, 1, 5, 9
#    numbers[3:4] = 1, 5
#    5 in numbers = 9
#    7 in numbers = False
#    "3" in numbers = 3
#    numbers + [6, 5, 3] = 14

#Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(numbers)

#Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

#Get all the elements from numbers except the first two (slice)
numbers = numbers[2:]
print(numbers)

#Check if 9 is an element of numbers
nine = 9 in numbers
print(nine)

