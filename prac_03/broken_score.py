
def main():
    score = float(input("Enter score: "))
    print(score_parameter(score))

def score_parameter(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score > 50:
        return "Average"
    else:
        return "Bad"

main()

