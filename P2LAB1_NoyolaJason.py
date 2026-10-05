# Jason Noyola
# 10/05/2026
# P2LAB1
# This program asks the user for the radius of a circle
# and calculates the diameter, circumference, and area.

# Pseudocode:
# Ask the user to enter the radius of a circle
# Convert the radius entered by the user into a float
# Calculate the diameter by multiplying the radius by 2
# Calculate the circumference using 2 * pi * radius
# Calculate the area using pi * radius squared
# Display the diameter with 1 decimal place
# Display the circumference with 2 decimal places
# Display the area with 3 decimal places

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print(f"The diameter of the circle is {diameter:.1f}")
print()
print(f"The circumference of the circle is {circumference:.2f}")
print()
print(f"The area of the circle is {area:.3f}")
