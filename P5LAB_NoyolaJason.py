# Jason Noyola
# November 22, 2026
# P5LAB - Self-Checkout Machine
# Simulates a customer paying for a purchase and calculates the change
# using the fewest dollars, quarters, dimes, nickels, and pennies.
#
# Pseudocode:
# 1. Import the random module.
# 2. Define disperse_change(change) to convert change to cents.
# 3. Count and display dollars, quarters, dimes, nickels, and pennies.
# 4. In main(), generate a random total owed from $0.01 to $100.00.
# 5. Ask the customer to enter the cash amount as a float.
# 6. If the amount is invalid or insufficient, ask again.
# 7. Subtract the total owed from cash received to find change.
# 8. Call disperse_change(change) to display the change breakdown.
# 9. Call main() to start the program.

import random


def disperse_change(change):
    """Display the fewest bills and coins needed for the change amount."""
    # Convert to integer cents to avoid floating-point rounding problems.
    cents = round(change * 100)

    if cents == 0:
        print("No change")
        return

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    pennies = cents % 5

    print("Change breakdown:")
    if dollars > 0:
        print(f"{dollars} {'Dollar' if dollars == 1 else 'Dollars'}")
    if quarters > 0:
        print(f"{quarters} {'Quarter' if quarters == 1 else 'Quarters'}")
    if dimes > 0:
        print(f"{dimes} {'Dime' if dimes == 1 else 'Dimes'}")
    if nickels > 0:
        print(f"{nickels} {'Nickel' if nickels == 1 else 'Nickels'}")
    if pennies > 0:
        print(f"{pennies} {'Penny' if pennies == 1 else 'Pennies'}")


def main():
    print("P5LAB - Self-Checkout Machine")
    print("Student: Jason Noyola")

    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"\nTotal owed: ${total_owed:.2f}")

    while True:
        try:
            cash_received = float(input("Enter the amount of cash you will insert: $"))
        except ValueError:
            print("Invalid entry. Please enter a number.")
            continue

        if cash_received < total_owed:
            print("Not enough cash. Please enter an amount that covers the total.")
        else:
            break

    change = round(cash_received - total_owed, 2)
    print(f"\nChange owed: ${change:.2f}")
    disperse_change(change)


if __name__ == "__main__":
    main()
