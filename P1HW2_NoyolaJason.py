# Jason Noyola
# September 20, 2026
# P1HW2 - Travel Expense
# This program calculates and displays travel expenses.

# Pseudocode:
# START
# Ask user to enter travel budget
# Ask user to enter travel destination
# Ask user to enter amount for gas
# Ask user to enter amount for accommodation
# Ask user to enter amount for food
# Add gas, accommodation, and food to get total expenses
# Subtract total expenses from the budget
# Display destination, budget, expenses, and remaining balance
# END

print("This program calculates and displays travel expenses")

# Get budget from user
budget = float(input("\nEnter Budget: "))

# Get travel destination from user
destination = input("\nEnter your travel destination: ")

# Get gas expense
gas = float(input("\nHow much do you think you will spend on gas? "))

# Get accommodation expense
accommodation = float(
    input("\nApproximately, how much will you need for accommodation/hotel? ")
)

# Get food expense
food = float(input("\nLast, how much do you need for food? "))

# Calculate total expenses
total_expenses = gas + accommodation + food

# Calculate remaining balance
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)

print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)

print("\nRemaining Balance:", remaining_balance)
