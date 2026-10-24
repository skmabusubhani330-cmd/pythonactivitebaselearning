
# Progressive Electricity Billing System

# Electricity rates per unit (example rates)
SLABS = [
    (100, 3.00),       # First 100 units: Rs. 3 per unit
    (200, 5.00),       # Next 200 units: Rs. 5 per unit
    (300, 7.00),       # Next 300 units: Rs. 7 per unit
    (float("inf"), 9.00)  # Above 600 units: Rs. 9 per unit
]

FIXED_CHARGE = 100.00
SURCHARGE_RATE = 0.05    # 5% surcharge
REBATE_RATE = 0.02       # 2% rebate
INCREASE_LIMIT = 30      # Alert if bill increases by over 30%


def calculate_energy_charge(units):
    """Calculate charges using progressive consumption slabs."""
    remaining_units = units
    energy_charge = 0
    previous_limit = 0

    for limit, rate in SLABS:
        slab_units = min(remaining_units, limit - previous_limit)
        if slab_units <= 0:
            break

        energy_charge += slab_units * rate
        remaining_units -= slab_units
        previous_limit = limit

        if remaining_units <= 0:
            break

    return energy_charge


def calculate_bill(units):
    """Calculate the complete electricity bill."""
    energy_charge = calculate_energy_charge(units)

    subtotal = energy_charge + FIXED_CHARGE
    surcharge = subtotal * SURCHARGE_RATE
    rebate = subtotal * REBATE_RATE

    total_bill = subtotal + surcharge - rebate

    return {
        "units": units,
        "energy_charge": energy_charge,
        "fixed_charge": FIXED_CHARGE,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total_bill
    }


def main():
    monthly_bills = {}

    print("=== PROGRESSIVE ELECTRICITY BILLING ===")

    try:
        months = int(input("Enter number of months to compare: "))

        if months < 1:
            print("Please enter at least one month.")
            return

        for i in range(months):
            month = input(f"\nEnter month {i + 1} name: ").strip()

            if not month:
                print("Month name cannot be empty.")
                return

            if month in monthly_bills:
                print("Duplicate month name. Please restart with unique names.")
                return

            units = float(input(f"Enter units consumed in {month}: "))

            if not 0 <= units < float("inf"):
                print("Units must be a non-negative finite number.")
                return

            monthly_bills[month] = calculate_bill(units)

    except ValueError:
        print("Invalid input. Enter valid numbers.")
        return

    # Display monthly bill details
    print("\n" + "=" * 75)
    print("MONTHLY ELECTRICITY BILL REPORT")
    print("=" * 75)

    for month, bill in monthly_bills.items():
        print(f"\nMonth: {month}")
        print(f"Units Consumed : {bill['units']:.2f}")
        print(f"Energy Charge  : Rs. {bill['energy_charge']:.2f}")
        print(f"Fixed Charge   : Rs. {bill['fixed_charge']:.2f}")
        print(f"Surcharge      : Rs. {bill['surcharge']:.2f}")
        print(f"Rebate         : Rs. {bill['rebate']:.2f}")
        print(f"Total Bill     : Rs. {bill['total']:.2f}")

    # Compare consecutive months
    print("\n" + "=" * 75)
    print("MONTH-TO-MONTH COMPARISON")
    print("=" * 75)

    previous_month = None

    for month, bill in monthly_bills.items():
        if previous_month is not None:
            previous_bill = monthly_bills[previous_month]["total"]
            current_bill = bill["total"]

            difference = current_bill - previous_bill

            if previous_bill > 0:
                percentage = (difference / previous_bill) * 100
            elif current_bill > 0:
                percentage = float("inf")
            else:
                percentage = 0

            print(f"\n{previous_month} -> {month}")
            print(f"Previous Bill : Rs. {previous_bill:.2f}")
            print(f"Current Bill  : Rs. {current_bill:.2f}")
            print(f"Difference    : Rs. {difference:.2f}")

            if percentage == float("inf"):
                print("Change        : New bill after a zero bill")
            else:
                print(f"Percentage    : {percentage:.2f}%")

            if percentage > INCREASE_LIMIT:
                print("ALERT: Unusual increase in electricity bill!")
            elif difference < 0:
                print("Bill decreased compared with previous month.")
            else:
                print("No unusual increase detected.")

        previous_month = month

    # Find the highest bill
    highest_month = max(
        monthly_bills,
        key=lambda m: monthly_bills[m]["total"]
    )

    print("\n" + "=" * 75)
    print("HIGHEST BILL")
    print("=" * 75)
    print(f"Month      : {highest_month}")
    print(f"Total Bill : Rs. {monthly_bills[highest_month]['total']:.2f}")


if __name__ == "__main__":
    main()
