# Student_Ave_Calc.py
# This program calculates the average mark for three quizzes
# It also allows multiple students' marks to be entered.

# Initialize the loop control variable
continue_choice = "Y"

# Repeat the program while the user enters Y
while continue_choice.upper() == "Y":

    # Display program title
    print("\nStudent Average Calculator")

    # Get the three quiz marks from the user
    quiz1 = float(input("Enter Quiz 1 mark: "))
    quiz2 = float(input("Enter Quiz 2 mark: "))
    quiz3 = float(input("Enter Quiz 3 mark: "))

    # Calculate the average mark
    average = (quiz1 + quiz2 + quiz3) / 3

    # Display the average rounded to 2 decimal places
    print("\nAverage Mark:", round(average, 2))

    # Determine whether the student passes or fails
    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    # Ask if another student's marks should be entered
    continue_choice = input(
        "\nDo you want to enter another student's marks? (Y/N): "
    )

# Display message when the program ends
print("\nProgram Ended.")