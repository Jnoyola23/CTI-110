# Name: Jason Noyola
# Date: 10/18/2026
# P3HW2 - Employee Pay Calculator

# Pseudocode:
# 1. Get employee name, hours worked, and pay rate
# 2. Check if employee worked over 40 hours
# 3. Calculate overtime hours and overtime pay
# 4. Calculate regular pay
# 5. Calculate gross pay
# 6. Display payroll results

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate regular and overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("-----------------------------------")
print(f"Employee name: {employee_name}")
print()
print(f"{'Hours Worked':<16}{'Pay Rate':<14}{'OverTime':<14}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
print("-" * 95)
print(f"{hours_worked:<16.1f}{pay_rate:<14.1f}{overtime_hours:<14.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:.2f}")
