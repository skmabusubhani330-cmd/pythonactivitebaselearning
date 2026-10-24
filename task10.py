
import math


def calculate_event_budget(
    venue_cost,
    equipment_cost,
    catering_per_person,
    transport_per_person,
    certificate_per_person,
    expected_participants,
    registration_fee,
    sponsorship
):
    # Validate inputs
    values = [
        venue_cost, equipment_cost, catering_per_person,
        transport_per_person, certificate_per_person,
        registration_fee, sponsorship
    ]

    if any(value < 0 for value in values):
        raise ValueError("Costs, fees, and sponsorship cannot be negative.")

    if expected_participants <= 0:
        raise ValueError("Expected participants must be positive.")

    # Fixed costs
    fixed_cost = venue_cost + equipment_cost

    # Variable costs per participant
    variable_cost_per_person = (
        catering_per_person
        + transport_per_person
        + certificate_per_person
    )

    # Total event costs
    variable_cost = variable_cost_per_person * expected_participants
    total_cost = fixed_cost + variable_cost

    # Financial contributions
    participant_contribution = registration_fee * expected_participants
    total_funding = participant_contribution + sponsorship

    # Sponsorship shortfall after participant fees and sponsorship
    funding_shortfall = max(0, total_cost - total_funding)
    surplus = max(0, total_funding - total_cost)

    # Remaining amount needed from sponsorship after registration fees
    required_sponsorship = max(0, total_cost - participant_contribution)

    # Minimum registrations required to break even
    # Sponsorship is assumed to be fixed.
    contribution_margin = registration_fee - variable_cost_per_person

    if total_cost <= sponsorship:
        break_even_registrations = 0
    elif contribution_margin > 0:
        break_even_registrations = max(
            0,
            math.ceil((fixed_cost - sponsorship) / contribution_margin)
        )
    else:
        break_even_registrations = None

    # Cost per participant at the expected attendance
    cost_per_participant = total_cost / expected_participants

    return {
        "fixed_cost": fixed_cost,
        "variable_cost_per_person": variable_cost_per_person,
        "variable_cost": variable_cost,
        "total_cost": total_cost,
        "expected_participants": expected_participants,
        "participant_contribution": participant_contribution,
        "sponsorship": sponsorship,
        "total_funding": total_funding,
        "required_sponsorship": required_sponsorship,
        "funding_shortfall": funding_shortfall,
        "surplus": surplus,
        "break_even_registrations": break_even_registrations,
        "cost_per_participant": cost_per_participant
    }


def display_report(report):
    print("\n" + "=" * 55)
    print("       CAMPUS EVENT FINANCIAL REPORT")
    print("=" * 55)

    print("\n--- Event Expenses ---")
    print(f"Fixed Costs              : Rs. {report['fixed_cost']:.2f}")
    print(f"Variable Cost per Person : Rs. {report['variable_cost_per_person']:.2f}")
    print(f"Total Variable Costs     : Rs. {report['variable_cost']:.2f}")
    print(f"Total Event Cost         : Rs. {report['total_cost']:.2f}")
    print(f"Cost per Participant     : Rs. {report['cost_per_participant']:.2f}")

    print("\n--- Funding Details ---")
    print(f"Expected Participants    : {report['expected_participants']}")
    print(f"Registration Contributions: Rs. {report['participant_contribution']:.2f}")
    print(f"Sponsorship              : Rs. {report['sponsorship']:.2f}")
    print(f"Total Available Funding  : Rs. {report['total_funding']:.2f}")
    print(f"Sponsorship Needed       : Rs. {report['required_sponsorship']:.2f}")

    print("\n--- Financial Analysis ---")
    if report["funding_shortfall"] > 0:
        print(f"Funding Shortfall        : Rs. {report['funding_shortfall']:.2f}")
        print("Status                   : Additional funding required")
    else:
        print(f"Financial Surplus        : Rs. {report['surplus']:.2f}")
        print("Status                   : Event is financially covered")

    if report["break_even_registrations"] is None:
        print("Break-even Registrations : Not possible at this fee")
        print("Increase the registration fee or secure more sponsorship.")
    else:
        print(
            "Minimum Registrations    : "
            f"{report['break_even_registrations']}"
        )

    print("=" * 55)


# Main program
print("CAMPUS EVENT FINANCIAL PLANNING")

venue_cost = float(input("Enter venue cost (Rs.): "))
equipment_cost = float(input("Enter equipment cost (Rs.): "))
catering = float(input("Enter catering cost per participant (Rs.): "))
transport = float(input("Enter transport cost per participant (Rs.): "))
certificate = float(input("Enter certificate cost per participant (Rs.): "))
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant (Rs.): "))
sponsorship = float(input("Enter confirmed sponsorship amount (Rs.): "))

report = calculate_event_budget(
    venue_cost,
    equipment_cost,
    catering,
    transport,
    certificate,
    participants,
    registration_fee,
    sponsorship
)

display_report(report)
