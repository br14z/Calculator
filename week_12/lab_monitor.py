# Function to check the status of five computers
def check_computers():
    computers = []  # Empty list to store computer statuses

    # Repeat the process for five computers
    for number in range(1, 6):

        # Ask the technician to enter the computer status
        status = input(
            f"Computer {number} Status (A/U/M): "
        ).upper()

        # Ensure that the entered status is valid
        while status not in ["A", "U", "M"]:
            print("Invalid status. Please enter A, U, or M.")

            status = input(
                f"Computer {number} Status (A/U/M): "
            ).upper()

        # Add the status to the computers list
        computers.append(status)

    return computers


# Function to count the available computers
def count_available(computers):
    available = 0  # Initial number of available computers

    # Check every status stored in the list
    for status in computers:

        # Increase the count when the computer is available
        if status == "A":
            available += 1

    return available


# Function to display the computer lab status
def display_status(computers, available):
    print("\n============ LAB STATUS ============")

    # Display the number and status of every computer
    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")

    print("====================================")
    print(f"Available Computers: {available}")
    print("====================================")