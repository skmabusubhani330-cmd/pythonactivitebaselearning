
# Employee Payroll and Deduction Analysis

def calculate_payroll():
    print("=" * 45)
    print("       EMPLOYEE PAYROLL SYSTEM")
    print("=" * 45)

    # Employee details
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")

    # Salary inputs
    basic_pay = float(input("Enter Basic Pay (Rs.): "))
    allowances = float(input("Enter Allowances (Rs.): "))
    overtime_hours = float(input("Enter Overtime Hours: "))
    overtime_rate = float(input("Enter Overtime Rate per Hour (Rs.): "))
    incentives = float(input("Enter Incentives (Rs.): "))

    # Validate inputs
    if (basic_pay < 0 or allowances < 0 or
            overtime_hours < 0 or overtime_rate < 0 or
            incentives < 0):
        print("\nError: Salary values cannot be negative.")
        return

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross_salary = (
        basic_pay + allowances + overtime_pay + incentives
    )

    # Progressive deductions
    # Illustrative monthly deduction policy
    if gross_salary <= 15000:
        tax = gross_salary * 0.05
    elif gross_salary <= 30000:
        tax = 15000 * 0.05 + (gross_salary - 15000) * 0.10
    elif gross_salary <= 60000:
        tax = (
            15000 * 0.05
            + 15000 * 0.10
            + (gross_salary - 30000) * 0.15
        )
    else:
        tax = (
            15000 * 0.05
            + 15000 * 0.10
            + 30000 * 0.15
            + (gross_salary - 60000) * 0.20
        )

    # Other deductions
    provident_fund = basic_pay * 0.12
    insurance = 500

    total_deductions = tax + provident_fund + insurance

    # Net salary
    net_salary = gross_salary - total_deductions

    # Display salary statement
    print("\n" + "=" * 45)
    print("          SALARY STATEMENT")
    print("=" * 45)
    print(f"Employee ID          : {emp_id}")
    print(f"Employee Name        : {emp_name}")
    print("-" * 45)

    print(f"Basic Pay            : Rs. {basic_pay:,.2f}")
    print(f"Allowances            : Rs. {allowances:,.2f}")
    print(f"Overtime Pay          : Rs. {overtime_pay:,.2f}")
    print(f"Incentives            : Rs. {incentives:,.2f}")
    print("-" * 45)
    print(f"Gross Salary          : Rs. {gross_salary:,.2f}")

    print("\nDEDUCTIONS")
    print("-" * 45)
    print(f"Progressive Tax       : Rs. {tax:,.2f}")
    print(f"Provident Fund (12%)  : Rs. {provident_fund:,.2f}")
    print(f"Insurance             : Rs. {insurance:,.2f}")
    print(f"Total Deductions      : Rs. {total_deductions:,.2f}")

    print("-" * 45)
    print(f"NET SALARY            : Rs. {net_salary:,.2f}")
    print("=" * 45)


calculate_payroll()
