"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter how much you sold: "))
while sales <= 0:
    print("Invalid, try again.")
    sales = float(input("Enter how much you sold: "))
if sales < 1000:
    bonus_below = sales * 0.1
    print("You get a 10% bonus, which equals to {:.2f}".format(sales + bonus_below))
elif sales >= 1000:
    bonus_above = sales * 0.15
    print("You get a 15% bonus, which equals to {:.2f}".format(sales + bonus_above))