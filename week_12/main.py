# Import the functions from the lab_monitor module
from lab_monitor import (
    check_computers,
    count_available,
    display_status
)


# Control whether the monitoring process should continue
continue_monitoring = "Y"

# Continue monitoring while the technician enters Y
while continue_monitoring == "Y":

    # Check and store the status of the five computers
    computers = check_computers()

    # Count the available computers
    available = count_available(computers)

    # Display the final lab status
    display_status(computers, available)

    # Ask the technician whether another cycle is needed
    continue_monitoring = input(
        "\nPerform another monitoring cycle? (Y/N): "
    ).upper()

print("\nComputer Lab Monitoring System ended.")