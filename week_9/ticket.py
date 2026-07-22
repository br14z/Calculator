"""Functions used to collect the details of a new helpdesk ticket."""


def create_ticket():
    """Ask the student for ticket details and return them to main.py."""

    # Display the system title.
    print("=== IT Helpdesk Ticket ===")

    # Ask the user to enter the ticket information.
    # strip() removes unnecessary spaces before or after the input.
    student_name = input("Student Name: ").strip()
    student_id = input("Student ID: ").strip()
    issue = input("Issue: ").strip()
    location = input("Location: ").strip()

    # Continue asking until the user enters a valid priority.
    while True:
        priority = input("Priority (High/Medium/Low): ").strip().capitalize()

        # Check whether the priority is valid.
        if priority in ("High", "Medium", "Low"):
            break

        print("Invalid priority. Please enter High, Medium, or Low.")

    # Store and return all the ticket information in a dictionary.
    return {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
    }