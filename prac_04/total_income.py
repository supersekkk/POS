
monthly_income = []


def main():
    number_of_months = int(input(("How many months?")))
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}:"))
        monthly_income.append(income)
    print_report(number_of_months)


def print_report(number_of_months):
    print("\nIncome report\n-----------\n")
    total_income = 0
    for month in range(1, number_of_months + 1):
        income = monthly_income[month - 1]
        total_income += income
        print(f"Month {month}: - Income: $  {income}      Total:   {total_income}")

    print(monthly_income)


main()