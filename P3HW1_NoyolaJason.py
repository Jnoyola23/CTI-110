# Name: Jason Noyola
# Date: 10/18/2026
# Assignment: P3HW1 - Debugging
# Description: Calculate the lowest, highest, sum,
# average, and letter grade for six module grades.

# PSEUDOCODE
# START
# Ask user to enter six module grades
# Store the six grades in a list
# Find the lowest grade
# Find the highest grade
# Calculate the sum of all grades
# Calculate the average of the grades
# Display the lowest, highest, sum, and average
# IF average is 90 or higher, display A
# ELSE IF average is 80 or higher, display B
# ELSE IF average is 70 or higher, display C
# ELSE IF average is 60 or higher, display D
# ELSE display F
# END

# Enter grades for six modules
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print("\n----------Results----------")
print(f"Lowest Grade:    {low:.1f}")
print(f"Highest Grade:   {high:.1f}")
print(f"Sum of Grades:   {total:.1f}")
print(f"Average:         {avg:.2f}")
print("--------------------------------------")

# Determine letter grade for average
if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
