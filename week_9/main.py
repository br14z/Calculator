"""Main program for the IT Helpdesk Ticket Registration System."""

# Import the display function from display.py.
from display import display_ticket

# Import the ticket creation function from ticket.py.
from ticket import create_ticket


def main():
    """Create a ticket, assign a technician, and display the result."""

    # Call create_ticket() and receive the returned dictionary.
    ticket = create_ticket()

    # Assign a technician according to the selected priority.
    if ticket["priority"] == "High":
        technician = "Ahmad"

    elif ticket["priority"] == "Medium":
        technician = "Hozaifa"

    else:
        technician = "Ali"

    # Send the ticket and technician to display.py.
    display_ticket(ticket, technician)


# Run main() only when main.py is executed directly.
if __name__ == "__main__":
    main()