for i in range(1, 21, 2):
    print(i, end=' ')
print()

 A:
for i in range(0, 101, 10):
    print(i, end=' ')
print()

 B:
 for i in range(20, 0, -1):
    print(i, end=' ')
 print()

 C:
stars = int(input("How many stars would you like to draw?"))
print("*" * stars)

 D:
rows = int(input("How many rows would you like?"))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end='')
#   print()

