password = (input("Type your password"))

if len(password) < 6:
    print("Too short")
elif len(password) > 15:
    print("Too long")

print(len(password) * "*")

