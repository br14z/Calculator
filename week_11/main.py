# ============================================
# main.py
# Purpose:
# Main program that connects all modules.
# ============================================

# Import functions from other modules
from student import get_student
from access import check_access, get_reason
from display import print_result

# Step 1: Get student information
name, student_id, registered, lab_open, computer_available = get_student()

# Step 2: Check whether access is granted
access = check_access(registered, lab_open, computer_available)

# Step 3: Decide the status message
if access:
    status = "Access Granted"
else:
    status = "Access Denied"

# Step 4: Get the reason
reason = get_reason(registered, lab_open, computer_available)

# Step 5: Display the final result
print_result(name, student_id, status, reason)