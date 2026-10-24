
# Hospital Billing and Patient Classification System

def calculate_bill():
    print("===== HOSPITAL BILLING SYSTEM =====")

    # Patient details
    patient_name = input("Enter patient name: ")
    patient_id = input("Enter patient ID: ")

    # Input charges
    consultation = float(input("Enter consultation charge: ₹"))
    diagnostic = float(input("Enter diagnostic charge: ₹"))
    treatment = float(input("Enter treatment charge: ₹"))

    # Validate billing constraints
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Error: Charges cannot be negative.")
        return

    if consultation + diagnostic + treatment == 0:
        print("Error: Total bill must be greater than zero.")
        return

    # Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Apply conditional concessions
    concession = 0

    if total_bill >= 10000:
        concession = total_bill * 0.15  # 15% concession
    elif total_bill >= 5000:
        concession = total_bill * 0.10  # 10% concession
    elif total_bill >= 2000:
        concession = total_bill * 0.05  # 5% concession

    # Calculate final bill
    final_bill = total_bill - concession

    # Patient classification based on payment policy
    print("\nSelect payment category:")
    print("1. Cash")
    print("2. Insurance")
    print("3. Government Scheme")
    print("4. Credit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        category = "Self-Pay / Cash Patient"
        payment_status = "Payment due immediately"
    elif choice == "2":
        category = "Insurance Patient"
        payment_status = "Subject to insurance approval"
    elif choice == "3":
        category = "Government Scheme Patient"
        payment_status = "Subject to scheme eligibility"
    elif choice == "4":
        category = "Credit Patient"
        payment_status = "Payment deferred"
    else:
        print("Invalid payment category.")
        return

    # Display billing report
    print("\n========== BILLING REPORT ==========")
    print("Patient Name       :", patient_name)
    print("Patient ID         :", patient_id)
    print("------------------------------------")
    print(f"Consultation Charge: ₹{consultation:.2f}")
    print(f"Diagnostic Charge  : ₹{diagnostic:.2f}")
    print(f"Treatment Charge   : ₹{treatment:.2f}")
    print("------------------------------------")
    print(f"Total Bill         : ₹{total_bill:.2f}")
    print(f"Concession         : ₹{concession:.2f}")
    print(f"Final Amount       : ₹{final_bill:.2f}")
    print("------------------------------------")
    print("Patient Category   :", category)
    print("Payment Status     :", payment_status)
    print("====================================")


calculate_bill()
