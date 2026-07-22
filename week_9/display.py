"""Functions used to display a completed helpdesk ticket."""


def display_ticket(ticket, technician):
    """Display the ticket details in a clear format."""

    # Print the completed helpdesk ticket.
    print("\n========== HELPDESK TICKET ==========")

    # Access each value from the ticket dictionary.
    print(f"Student Name : {ticket['student_name']}")
    print(f"Student ID   : {ticket['student_id']}")
    print(f"Issue        : {ticket['issue']}")
    print(f"Location     : {ticket['location']}")
    print(f"Priority     : {ticket['priority']}")

    # Display the technician selected by main.py.
    print(f"Technician   : {technician}")

    # Every newly created ticket begins with Pending status.
    print("Status       : Pending")
    print("=====================================")