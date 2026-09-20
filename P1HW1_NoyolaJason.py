# Jason Noyola
# September 20, 2026
# P1HW1 - Mathematical Expressions
# This program asks the user for integers and performs exponent, addition, and subtraction calculations.

print("-----Calculating Exponents-----")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(f"{base} raised to the power of {exponent} is {result} !!")

print()
print("-----Addition and Subtraction-----")
print()

starting_integer = int(input("Enter a starting integer: "))
integer_to_add = int(input("Enter an integer to add: "))
integer_to_subtract = int(input("Enter an integer to subtract: "))

final_result = starting_integer + integer_to_add - integer_to_subtract

print()
print(
    f"{starting_integer} + {integer_to_add} - "
    f"{integer_to_subtract} is equal to {final_result}"
)
