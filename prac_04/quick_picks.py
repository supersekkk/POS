
import random


MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_PER_LINE = 6


def main():
    quick_pick = int(input("How many quick picks would you like?"))
    while quick_pick < 0:
        print("Makes no sense!")
        quick_pick = int(input("How many quick picks would you like?"))

    for i in range(quick_pick):
        quick_pick_list = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER,MAX_NUMBER)
            while number in quick_pick_list:
                number = random.randint(MIN_NUMBER,MAX_NUMBER)
            quick_pick_list.append(number)
        quick_pick_list.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick_list))
main()