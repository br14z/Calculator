# Student_Ave_Calc.py

continue_choice = "Y"

while continue_choice.upper() == "Y":

    print("\nStudent Average Calculator")

    quiz1 = float(input("Enter Quiz 1 mark: "))
    quiz2 = float(input("Enter Quiz 2 mark: "))
    quiz3 = float(input("Enter Quiz 3 mark: "))

    average = (quiz1 + quiz2 + quiz3) / 3

    print("\nAverage Mark:", round(average, 2))

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    continue_choice = input("\nDo you want to enter another student's marks? (Y/N): ")

print("\nProgram Ended.")