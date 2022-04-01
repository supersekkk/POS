"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A valueError will occur when you try to assign an invalid value to a function

2. When will a ZeroDivisionError occur?
When you try to devide something by zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I guess you could use an if-statement, if  or denominator = 0, create a loop and try again

Update: I tried to do this, but it did not work. I still got zerodivisionerror
"""


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")