
number_of_numbers = 5
list_of_numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    for i in range(0, number_of_numbers):
        user_numbers = input("What numbers would you like to add?")
        list_of_numbers.append(user_numbers)
    interesting_display()
    check_username()

def interesting_display():

    print(f"The first number is {(list_of_numbers[0])}")
    print(f"The last number is {(list_of_numbers[-1])}")
    print(f"The smallest number is {min(list_of_numbers)}")
    print(f"The biggest number is {max(list_of_numbers)}")
    print(list_of_numbers)
    convert_numbers = [int(i) for i in list_of_numbers]
    print(sum(convert_numbers) // (number_of_numbers))

def check_username():
    username = input("What is your username?")
    if username not in usernames:
        print("Access denied")
        input("Try again. What is your username?")
        check_username()
    else:
        print("Access granted")



main()