# Name: Jason Noyola
# Date: 11/01/2026
# Assignment: P4LAB2
# Description: Display a multiplication table for a
# non-negative integer and allow the user to run
# the program again.

# PSEUDOCODE
# 1. Start the program.
# 2. Set the run_again variable to "yes".
# 3. WHILE run_again equals "yes":
#    a. Ask the user to enter an integer.
#    b. IF the integer is 0 or greater:
#       - Use a FOR loop from 1 through 12.
#       - Multiply the integer by each number.
#       - Display each multiplication result.
#    c. ELSE:
#       - Display that negative values are not accepted.
#    d. Ask the user if they want to run again.
#    e. IF the answer is "no", end the loop.
# 4. End the program.

run_again = "yes"

while run_again == "yes":
    number = int(input("Enter an integer: "))

    if number >= 0:
        for i in range(1, 13):
            result = number * i
            print(f"{number} * {i} = {result}")
    else:
        print("Negative values are not accepted.")

    run_again = input(
        "Would you like to run the program again? "
    ).lower()

print("Program ended.")
