# ============================================
# access.py
# Purpose:
# Check whether the student can access the lab
# and determine the reason.
# ============================================

def check_access(registered, lab_open, computer_available):
    """
    Returns True if all conditions are satisfied.
    Otherwise returns False.
    """

    if (
        registered == "Y"
        and lab_open == "Y"
        and computer_available == "Y"
    ):
        return True
    else:
        return False


def get_reason(registered, lab_open, computer_available):
    """
    Returns the appropriate reason based on
    the student's answers.
    """

    if registered != "Y":
        return "Student is not registered"

    elif lab_open != "Y":
        return "Computer lab is closed"

    elif computer_available != "Y":
        return "No available computer"

    else:
        return "Welcome to the lab"