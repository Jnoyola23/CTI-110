# Jason Noyola
# 10/05/2026
# P2HW2
# This program asks the user for six module grades,
# stores them in a list, and calculates the lowest grade,
# highest grade, sum, and average.

"""
Pseudocode:

START

Ask user to enter grade for Module 1
Ask user to enter grade for Module 2
Ask user to enter grade for Module 3
Ask user to enter grade for Module 4
Ask user to enter grade for Module 5
Ask user to enter grade for Module 6

Store all six grades in a list called module_grades

Find the lowest grade in module_grades
Find the highest grade in module_grades
Calculate the sum of module_grades
Calculate the average by dividing the sum by 6

Display the results
Display lowest grade with one decimal place
Display highest grade with one decimal place
Display sum with one decimal place
Display average with two decimal places

END
"""

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_grades = sum(module_grades)
average = sum_grades / 6

print()
print("------------Results------------")
print(f"Lowest Grade:      {lowest_grade:.1f}")
print(f"Highest Grade:     {highest_grade:.1f}")
print(f"Sum of Grades:     {sum_grades:.1f}")
print(f"Average:           {average:.2f}")
print("--------------------------------")
