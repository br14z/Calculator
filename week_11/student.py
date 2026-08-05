# ============================================
# student.py
# Purpose:
# Collect student information from the user.
# ============================================

def get_student():
    # Display program title
    print("===== Computer Lab Access =====")

    # Ask the user to enter their name
    name = input("Student Name : ")

    # Ask for student ID
    student_id = input("Student ID : ")

    # Ask whether the student is registered
    registered = input("Registered for today's lab? (Y/N): ").upper()

    # Ask whether the lab is currently open
    lab_open = input("Is the lab open? (Y/N): ").upper()

    # Ask whether computers are available
    computer_available = input("Computer Available? (Y/N): ").upper()

    # Return all collected information to main.py
    return name, student_id, registered, lab_open, computer_available