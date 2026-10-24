# University Scholarship Allocation System

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 250000
SCHOLARSHIP_LIMIT = 5


def evaluate_eligibility(student):
    """Check whether a student satisfies all eligibility criteria."""

    reasons = []

    if student["aggregate"] < MIN_AGGREGATE:
        reasons.append("Aggregate marks below minimum")

    if any(mark < MIN_SUBJECT_MARKS for mark in student["subjects"]):
        reasons.append("Subject-wise marks below minimum")

    if student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Attendance below minimum")

    if student["income"] > MAX_FAMILY_INCOME:
        reasons.append("Family income exceeds limit")

    return len(reasons) == 0, reasons


def calculate_score(student):
    """
    Rank students using these tie-breaking priorities:
    1. Higher aggregate marks
    2. Higher attendance
    3. Lower family income
    4. Higher total subject marks
    5. Student ID in ascending order
    """

    return (
        -student["aggregate"],
        -student["attendance"],
        student["income"],
        -sum(student["subjects"]),
        student["id"]
    )


def allocate_scholarships(students):
    eligible = []
    rejected = []

    # Evaluate eligibility
    for student in students:
        status, reasons = evaluate_eligibility(student)

        if status:
            eligible.append(student)
        else:
            rejected.append((student, reasons))

    # Sort eligible students according to ranking rules
    eligible.sort(key=calculate_score)

    # Allocate scholarships to the top-ranked students
    selected = eligible[:SCHOLARSHIP_LIMIT]
    waiting_list = eligible[SCHOLARSHIP_LIMIT:]

    return selected, waiting_list, rejected


def display_results(selected, waiting_list, rejected):
    print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

    print("\n--- Selected Students ---")
    if selected:
        for rank, student in enumerate(selected, start=1):
            print(
                f"Rank {rank}: {student['name']} "
                f"(ID: {student['id']}) | "
                f"Aggregate: {student['aggregate']}% | "
                f"Attendance: {student['attendance']}% | "
                f"Income: Rs.{student['income']}"
            )
    else:
        print("No students selected.")

    print("\n--- Waiting List ---")
    if waiting_list:
        for rank, student in enumerate(
            waiting_list, start=len(selected) + 1
        ):
            print(
                f"Rank {rank}: {student['name']} "
                f"(ID: {student['id']})"
            )
    else:
        print("No students on the waiting list.")

    print("\n--- Rejected Applicants ---")
    if rejected:
        for student, reasons in rejected:
            print(f"{student['name']} (ID: {student['id']})")
            for reason in reasons:
                print(f"  - {reason}")
    else:
        print("No rejected applicants.")


def main():
    students = [
        {
            "id": 101,
            "name": "musalisalam",
            "aggregate": 92,
            "subjects": [95, 90, 91, 92],
            "attendance": 96,
            "income": 180000
        },
        {
            "id": 102,
            "name": "mabusubhani",
            "aggregate": 88,
            "subjects": [85, 90, 87, 90],
            "attendance": 92,
            "income": 200000
        },
        {
            "id": 103,
            "name": "ramsai",
            "aggregate": 88,
            "subjects": [90, 85, 88, 89],
            "attendance": 95,
            "income": 150000
        },
        {
            "id": 104,
            "name": "veldivignan",
            "aggregate": 72,
            "subjects": [75, 70, 72, 71],
            "attendance": 90,
            "income": 120000
        },
        {
            "id": 105,
            "name": "Ravindra",
            "aggregate": 85,
            "subjects": [80, 82, 78, 85],
            "attendance": 70,
            "income": 100000
        },
        {
            "id": 106,
            "name": "syamsai",
            "aggregate": 80,
            "subjects": [75, 82, 78, 85],
            "attendance": 85,
            "income": 230000
        },
        {
            "id": 107,
            "name": "gagan",
            "aggregate": 90,
            "subjects": [92, 88, 90, 91],
            "attendance": 94,
            "income": 220000
        }
    ]

    selected, waiting_list, rejected = allocate_scholarships(
        students
    )

    display_results(selected, waiting_list, rejected)


if __name__ == "__main__":
    main()

