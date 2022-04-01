"""input_file = "name.txt"

your_name = input("What is your name?")
input_file = open("name.txt", 'w')
print(your_name, file=input_file)
input_file.close()

output_file = open("name.txt", 'r')
print("Your name is", (output_file.read()))
output_file.close()"""

# NUMBERS
number_file = "numbers.txt"

#number = input("Which number would you like to add?")
#number_file = open("numbers.txt", 'a')
#print(number, file=number_file)
#number_file.close



"""This is the code for task 3

UPDATE : I DONT KNOW HOW TO SUM THE FIRST TWO NUMBERS. NEED TO ASK Q.
You can see that i tried several ways to make this work....
Consequently, i also struggled with task 4
Where is this in the powerpoints????
"""

number_file = open("numbers.txt", 'r')
output = number_file.readlines()
sum = 0

count = 0
for line in output:
    count += 1
    print("Number {}: {}".format(count, line.strip()))
number1 = number_file.readline()

print(output[0] + output[1])
total = (output[0] + output[1])
print(total)


# TASK 4