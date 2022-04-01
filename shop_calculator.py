""" I made this a little bit more advanced than I needed to. Could work on it to make it run smoother,
like the "No" exit and perhaps creating a menu - this is all the time I had today"""


inventory = []
total_price = 0
purchase = (input("What would you like to add to your inventory?"))
price = (int(input("What is the price?")))
total_price += price
while purchase != "No":
    inventory.append(purchase)
    purchase = (input("Would you like to buy something else?"))
    if purchase != "No":
        price = (int(input("What is the price?")))
        total_price += price


print("Number of items: {:.2f}".format(len(inventory)))
print("Price of items: {:.2f}".format(total_price))

discount = total_price * 0.1
total_discount = total_price * 0.9
if total_price > 100:
    print("You have deserved a 10% discount for shopping for more than 100$ !!")
    print("Your discount is {:.2f}, and your total discount is {:.2f}".format(discount, total_discount))

