
# Manufacturing Cost and Profitability Analysis

def calculate_manufacturing_cost(
    product_name,
    quantity,
    material_cost_per_unit,
    labour_cost_per_unit,
    wastage_percent,
    machine_cost_per_hour,
    machine_hours_per_unit,
    overhead_cost_per_unit,
    selling_price_per_unit,
    target_profit_percent
):
    # Validate inputs
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if any(value < 0 for value in [
        material_cost_per_unit,
        labour_cost_per_unit,
        wastage_percent,
        machine_cost_per_hour,
        machine_hours_per_unit,
        overhead_cost_per_unit,
        selling_price_per_unit,
        target_profit_percent
    ]):
        raise ValueError("Costs, prices, and percentages cannot be negative.")

    # 1. Calculate material cost
    material_cost = material_cost_per_unit * quantity

    # 2. Calculate wastage cost
    wastage_cost = material_cost * wastage_percent / 100

    # 3. Calculate labour cost
    labour_cost = labour_cost_per_unit * quantity

    # 4. Calculate machine cost
    machine_cost = (
        machine_cost_per_hour
        * machine_hours_per_unit
        * quantity
    )

    # 5. Calculate overhead cost
    overhead_cost = overhead_cost_per_unit * quantity

    # 6. Calculate total manufacturing cost
    total_cost = (
        material_cost
        + wastage_cost
        + labour_cost
        + machine_cost
        + overhead_cost
    )

    # 7. Calculate total revenue
    total_revenue = selling_price_per_unit * quantity

    # 8. Calculate profit or loss
    profit = total_revenue - total_cost

    # Profit margin as a percentage of revenue
    profit_margin = (
        (profit / total_revenue) * 100
        if total_revenue > 0 else 0
    )

    # Profit target as a percentage of total cost
    target_profit = total_cost * target_profit_percent / 100

    # 9. Check target profitability
    target_met = profit >= target_profit

    # 10. Calculate recommended selling price
    recommended_price = (
        total_cost / quantity
        * (1 + target_profit_percent / 100)
    )

    return {
        "product_name": product_name,
        "quantity": quantity,
        "material_cost": material_cost,
        "wastage_cost": wastage_cost,
        "labour_cost": labour_cost,
        "machine_cost": machine_cost,
        "overhead_cost": overhead_cost,
        "total_cost": total_cost,
        "cost_per_unit": total_cost / quantity,
        "total_revenue": total_revenue,
        "profit": profit,
        "profit_margin": profit_margin,
        "target_profit": target_profit,
        "target_met": target_met,
        "recommended_price": recommended_price
    }


def display_report(result):
    print("\n" + "=" * 55)
    print("       MANUFACTURING COST & PROFITABILITY REPORT")
    print("=" * 55)

    print(f"Product Name       : {result['product_name']}")
    print(f"Production Quantity: {result['quantity']}")

    print("\n--- Manufacturing Costs ---")
    print(f"Material Cost      : Rs. {result['material_cost']:.2f}")
    print(f"Wastage Cost       : Rs. {result['wastage_cost']:.2f}")
    print(f"Labour Cost        : Rs. {result['labour_cost']:.2f}")
    print(f"Machine Cost       : Rs. {result['machine_cost']:.2f}")
    print(f"Overhead Cost      : Rs. {result['overhead_cost']:.2f}")

    print("-" * 55)
    print(f"Total Production Cost: Rs. {result['total_cost']:.2f}")
    print(f"Cost Per Unit        : Rs. {result['cost_per_unit']:.2f}")

    print("\n--- Profitability Analysis ---")
    print(f"Total Revenue      : Rs. {result['total_revenue']:.2f}")
    print(f"Profit / Loss      : Rs. {result['profit']:.2f}")
    print(f"Profit Margin      : {result['profit_margin']:.2f}%")
    print(f"Required Profit    : Rs. {result['target_profit']:.2f}")
    print(
        f"Recommended Selling Price Per Unit: "
        f"Rs. {result['recommended_price']:.2f}"
    )

    print("\n--- Production Decision ---")
    if result["target_met"]:
        print("SUCCESS: Production meets the profit target.")
    elif result["profit"] < 0:
        print("WARNING: Production results in a loss.")
    else:
        print("WARNING: Production does not meet the profit target.")

    print("=" * 55)


# Main program
print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

product_name = input("Enter product name: ").strip()
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Material cost per unit (Rs.): "))
labour_cost = float(input("Labour cost per unit (Rs.): "))
wastage_percent = float(input("Material wastage percentage: "))

machine_cost = float(input("Machine cost per hour (Rs.): "))
machine_hours = float(input("Machine hours required per unit: "))

overhead_cost = float(input("Overhead cost per unit (Rs.): "))
selling_price = float(input("Selling price per unit (Rs.): "))

target_profit = float(input("Target profit percentage on cost: "))

result = calculate_manufacturing_cost(
    product_name,
    quantity,
    material_cost,
    labour_cost,
    wastage_percent,
    machine_cost,
    machine_hours,
    overhead_cost,
    selling_price,
    target_profit
)

display_report(result)
