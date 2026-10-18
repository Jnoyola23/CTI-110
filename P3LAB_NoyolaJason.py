# Name: Jason Noyola
#10/18/2026
# P3LAB - Making Change


# PSEUDOCODE
# START
# Ask user to enter an amount of money
# Convert money into cents by multiplying by 100
# Calculate dollars using integer division by 100
# Subtract dollar value from remaining cents
# Calculate quarters using integer division by 25
# Subtract quarter value from remaining cents
# Calculate dimes using integer division by 10
# Subtract dime value from remaining cents
# Calculate nickels using integer division by 5
# Subtract nickel value from remaining cents
# Remaining cents are pennies
# IF the number of coins is greater than zero
#     Display the number and coin name
#     Use singular name if the count is one
#     Otherwise use plural name
# IF the amount entered is zero
#     Display "No change"
# END

# Get amount from user
money = float(input("Enter the amount of money as a float: $"))

# Convert money to cents
cents = round(money * 100)

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Calculate pennies
pennies = cents

# Display dollars
if dollars == 1:
    print(dollars, "Dollar")
elif dollars > 1:
    print(dollars, "Dollars")

# Display quarters
if quarters == 1:
    print(quarters, "Quarter")
elif quarters > 1:
    print(quarters, "Quarters")

# Display dimes
if dimes == 1:
    print(dimes, "Dime")
elif dimes > 1:
    print(dimes, "Dimes")

# Display nickels
if nickels == 1:
    print(nickels, "Nickel")
elif nickels > 1:
    print(nickels, "Nickels")

# Display pennies
if pennies == 1:
    print(pennies, "Penny")
elif pennies > 1:
    print(pennies, "Pennies")

# Display no change if amount is zero
if money == 0:
    print("No change")
