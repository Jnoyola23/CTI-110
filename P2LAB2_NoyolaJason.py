# Jason Noyola
# 10/05/2026
# P2LAB2
# This program stores vehicles and their MPG in a dictionary.
# It allows the user to select a vehicle and calculates
# how many gallons of gas are needed for a trip.

# Pseudocode:
# Create a dictionary containing vehicle names and MPG values
# Create a variable that stores all the keys from the dictionary
# Display the available vehicle names
# Ask the user to enter one of the vehicle names
# Get the MPG for the vehicle selected by the user
# Display the MPG for the selected vehicle
# Ask the user how many miles they will drive
# Divide miles by MPG to calculate gallons of gas needed
# Display the gallons needed rounded to two decimal places

vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicle_mpg.keys()

print(keys)

vehicle = input("\nEnter a vehicle to see it's mpg: ")

mpg = vehicle_mpg[vehicle]

print(f"\nThe {vehicle} gets {mpg} mpg.")

miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

gallons = miles / mpg

print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
