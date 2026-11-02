# Name: Jason Noyola
# Date: 11/01/2026
# P4HW2 - Employee Pay Calculator
# Description: Calculate payroll for multiple employees.

# Pseudocode:
# 1. Set employee count and payroll totals to zero.
# 2. Ask for employee name or "Done" to finish.
# 3. While employee name is not "Done":
#    a. Ask for hours worked and pay rate.
#    b. Check if hours worked are over 40.
#    c. Calculate overtime hours and overtime pay.
#    d. Calculate regular pay.
#    e. Calculate gross pay.
#    f. Display employee payroll information.
#    g. Add employee pay to running totals.
#    h. Increase employee count by one.
#    i. Ask for the next employee.
# 4. Display final payroll totals.

# Initialize totals
employee_count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

# Ask for first employee
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Sentinel loop
while employee_name != "Done":

    # Get employee information
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

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

    # Display employee payroll
    print()
    print(f"Employee name:   {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<13}{'OverTime':<13}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
    print("-" * 95)
    print(f"{hours_worked:<15.1f}{pay_rate:<13.2f}{overtime_hours:<13.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:.2f}")
    print()

    # Update totals
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Display final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
