
# Multi-Currency Travel Budget Analysis

def analyze_travel_budget(expenses, exchange_rates, fee_percent, budget):
    converted_expenses = []
    category_totals = {}
    total_before_fees = 0
    total_fees = 0

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        currency = expense["currency"]

        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")

        if currency not in exchange_rates:
            raise ValueError(f"Exchange rate missing for {currency}")

        # Convert expense into base currency (INR)
        rate = exchange_rates[currency]
        converted_amount = amount * rate

        # Calculate currency conversion fee
        fee = converted_amount * fee_percent / 100
        final_amount = converted_amount + fee

        total_before_fees += converted_amount
        total_fees += fee

        # Calculate total expense by category
        category_totals[category] = (
            category_totals.get(category, 0) + final_amount
        )

        converted_expenses.append({
            "category": category,
            "description": expense["description"],
            "original_amount": amount,
            "currency": currency,
            "converted_amount": converted_amount,
            "fee": fee,
            "final_amount": final_amount
        })

    # Calculate total spending including fees
    total_spending = total_before_fees + total_fees

    # Compare spending against budget
    difference = budget - total_spending

    if difference > 0:
        budget_status = "Within budget"
    elif difference == 0:
        budget_status = "Budget fully used"
    else:
        budget_status = "Over budget"

    # Identify the largest expense category
    if category_totals:
        largest_category = max(
            category_totals,
            key=category_totals.get
        )
        largest_amount = category_totals[largest_category]
    else:
        largest_category = "None"
        largest_amount = 0

    return {
        "expenses": converted_expenses,
        "total_before_fees": total_before_fees,
        "total_fees": total_fees,
        "total_spending": total_spending,
        "budget": budget,
        "difference": difference,
        "budget_status": budget_status,
        "category_totals": category_totals,
        "largest_category": largest_category,
        "largest_amount": largest_amount
    }


def display_report(report):
    print("\n" + "=" * 90)
    print("             MULTI-CURRENCY TRAVEL BUDGET REPORT")
    print("=" * 90)

    print(
        f"{'Category':<15}{'Description':<20}{'Original':>12}"
        f"{'Converted':>14}{'Fee':>10}{'Total (INR)':>15}"
    )
    print("-" * 90)

    for item in report["expenses"]:
        original = (
            f"{item['original_amount']:.2f} "
            f"{item['currency']}"
        )

        print(
            f"{item['category']:<15}"
            f"{item['description']:<20}"
            f"{original:>12}"
            f"{item['converted_amount']:>14.2f}"
            f"{item['fee']:>10.2f}"
            f"{item['final_amount']:>15.2f}"
        )

    print("-" * 90)
    print(
        f"{'Total before fees:':<60}"
        f"Rs. {report['total_before_fees']:>12.2f}"
    )
    print(
        f"{'Total conversion fees:':<60}"
        f"Rs. {report['total_fees']:>12.2f}"
    )
    print(
        f"{'Total spending:':<60}"
        f"Rs. {report['total_spending']:>12.2f}"
    )
    print(f"{'Travel budget:':<60}Rs. {report['budget']:>12.2f}")

    if report["difference"] >= 0:
        print(
            f"{'Budget remaining:':<60}"
            f"Rs. {report['difference']:>12.2f}"
        )
    else:
        print(
            f"{'Amount over budget:':<60}"
            f"Rs. {-report['difference']:>12.2f}"
        )

    print(f"\nBudget status: {report['budget_status']}")

    print("\n--- Expense Category Summary ---")
    for category, amount in report["category_totals"].items():
        print(f"{category:<20}: Rs. {amount:.2f}")

    print(
        f"\nLargest Expense Category: "
        f"{report['largest_category']}"
    )
    print(
        f"Largest Category Spending: "
        f"Rs. {report['largest_amount']:.2f}"
    )
    print("=" * 90)


# Main program

# Exchange rates: amount of INR for one unit of foreign currency.
# These rates are illustrative; replace them with supplied rates.
exchange_rates = {
    "INR": 1.0,
    "USD": 84.0,
    "EUR": 92.0,
    "GBP": 110.0,
    "JPY": 0.56
}

expenses = []

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("Supported currencies:", ", ".join(exchange_rates.keys()))

budget = float(input("Enter total travel budget in INR: "))
fee_percent = float(input("Enter conversion fee percentage: "))
num_expenses = int(input("Enter number of expenses: "))

if budget < 0 or fee_percent < 0:
    raise ValueError("Budget and fee percentage cannot be negative.")

if num_expenses <= 0:
    raise ValueError("Enter at least one expense.")

for i in range(num_expenses):
    print(f"\nExpense {i + 1}")

    category = input("Enter category (Food/Hotel/Transport/Shopping): ").strip().title()
    description = input("Enter expense description: ").strip()
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency code: ").strip().upper()

    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")

    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {currency}")

    expenses.append({
        "category": category,
        "description": description,
        "amount": amount,
        "currency": currency
    })

report = analyze_travel_budget(
    expenses,
    exchange_rates,
    fee_percent,
    budget
)

display_report(report)
