
# Retail Billing with Multiple Discount Rules

# Category-specific tax rates (percentage)
TAX_RATES = {
    "Electronics": 18,
    "Clothing": 5,
    "Groceries": 0,
    "Furniture": 12
}

# Discount thresholds
DISCOUNT_RULES = [
    (10000, 15),  # 15% discount for subtotal >= 10000
    (5000, 10),   # 10% discount for subtotal >= 5000
    (2000, 5)     # 5% discount for subtotal >= 2000
]

MAX_CONCESSION = 2000  # Maximum discount in Rs.


def calculate_bill(products):
    subtotal = 0
    invoice_items = []

    # Calculate amount for each product
    for product in products:
        name = product["name"]
        category = product["category"]
        price = product["price"]
        quantity = product["quantity"]

        if price < 0 or quantity <= 0:
            raise ValueError("Price must be non-negative and quantity positive.")

        if category not in TAX_RATES:
            raise ValueError(f"Unknown category: {category}")

        amount = price * quantity
        tax_rate = TAX_RATES[category]
        tax_amount = amount * tax_rate / 100

        subtotal += amount

        invoice_items.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "amount": amount,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount
        })

    # Determine discount based on subtotal
    discount_rate = 0

    for threshold, rate in DISCOUNT_RULES:
        if subtotal >= threshold:
            discount_rate = rate
            break

    # Apply maximum concession limit
    discount = subtotal * discount_rate / 100
    discount = min(discount, MAX_CONCESSION)

    # Allocate discount proportionally across items
    for item in invoice_items:
        share = item["amount"] / subtotal if subtotal else 0
        item["discount"] = discount * share
        item["taxable_amount"] = item["amount"] - item["discount"]

        # Recalculate tax after discount
        item["tax_amount"] = (
            item["taxable_amount"] * item["tax_rate"] / 100
        )

    total_tax = sum(item["tax_amount"] for item in invoice_items)
    grand_total = subtotal - discount + total_tax

    return {
        "items": invoice_items,
        "subtotal": subtotal,
        "discount_rate": discount_rate,
        "discount": discount,
        "total_tax": total_tax,
        "grand_total": grand_total
    }


def print_invoice(bill):
    print("\n" + "=" * 90)
    print("                         RETAIL STORE INVOICE")
    print("=" * 90)

    print(
        f"{'Product':<16}{'Category':<14}{'Price':>9}"
        f"{'Qty':>5}{'Amount':>11}{'Discount':>11}{'Tax':>10}"
    )
    print("-" * 90)

    for item in bill["items"]:
        print(
            f"{item['name']:<16}"
            f"{item['category']:<14}"
            f"{item['price']:>9.2f}"
            f"{item['quantity']:>5}"
            f"{item['amount']:>11.2f}"
            f"{item['discount']:>11.2f}"
            f"{item['tax_amount']:>10.2f}"
        )

    print("-" * 90)
    print(f"{'Subtotal:':<65}Rs. {bill['subtotal']:>10.2f}")
    print(
        f"{'Discount (' + str(bill['discount_rate']) + '%):':<65}"
        f"Rs. {bill['discount']:>10.2f}"
    )
    print(f"{'Total Tax:':<65}Rs. {bill['total_tax']:>10.2f}")
    print("=" * 90)
    print(f"{'GRAND TOTAL:':<65}Rs. {bill['grand_total']:>10.2f}")
    print("=" * 90)


# Main program
products = []

num_products = int(input("Enter number of products: "))

if num_products <= 0:
    raise ValueError("Number of products must be positive.")

print("\nAvailable categories:", ", ".join(TAX_RATES.keys()))

for i in range(num_products):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip().title()
    price = float(input("Enter unit price (Rs.): "))
    quantity = int(input("Enter quantity: "))

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    })

bill = calculate_bill(products)
print_invoice(bill)
