# Jason Noyola
# 10/05/2026
# P2HW1
# This program calculates and displays travel expenses
# and the remaining balance from a travel budget.

# Pseudocode:
# Display a message explaining what the program does
# Ask the user to enter their travel budget
# Ask the user to enter their travel destination
# Ask the user how much they will spend on gas
# Ask the user how much they will spend on accommodation/hotel
# Ask the user how much they will spend on food
# Add gas, accommodation, and food expenses
# Subtract the total expenses from the travel budget
# Display the destination and all expenses in aligned columns
# Format all money values with a dollar sign and two decimal places
# Display the remaining balance

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

remaining_balance = budget - gas - accommodation - food

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("---------------------------------------")
print(f"\n{'Remaining Balance:':<20}${remaining_balance:.2f}")
