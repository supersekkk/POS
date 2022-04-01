"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0:
    print("Invalid score")
    score = float(input("Enter score: "))
else:
    if score > 100:
        print("Invalid score")
    elif 50 <= score <= 89:
        print("Passable")
    elif score >= 90:
        print("Excellent")
if score < 50:
    print("Bad")