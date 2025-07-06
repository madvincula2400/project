total_pay = 0
num_employees = 0

print("Payroll Calculator Program")
answer = input("Do you want to calculate payroll? (Yes to continue): ")

while answer == "Yes":
    name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter pay rate per hour: $"))

    if hours > 40:
        regular_pay = 40 * rate
        overtime_hrs = hours - 40
        overtime_pay = overtime_hrs * rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hours * rate

    print("Employee:", name)
    print("Gross Pay: $" + str(round(gross_pay, 2)))

    total_pay = total_pay + gross_pay
    num_employees = num_employees + 1

    answer = input("Do you want to enter another employee? (Yes to continue): ")

print()
print("Final Results:")
print("Number of employees:", num_employees)
print("Total gross pay: $" + str(round(total_pay, 2)))

if num_employees > 0:
    avg_pay = total_pay / num_employees
    print("Average pay: $" + str(round(avg_pay, 2)))

