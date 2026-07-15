# This function collects the customer's order information
def get_customer():

    # Display the customer information heading
    print("=== Customer Information ===")

    # Ask the user to enter the customer's name
    name = input("Customer Name : ")

    # Ask the user to enter the food ordered
    food = input("Food Ordered (Cake/Muffin) : ")

    # Convert the quantity into an integer
    quantity = int(input("Quantity : "))

    # Convert the price into a decimal number
    price = float(input("Price per Item (RM): "))

    # Ask whether the customer wants delivery
    delivery_choice = input("Delivery (Y/N): ")

    # Set the delivery charge based on the user's answer
    if delivery_choice.upper() == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00

    # Return all the information to the main program
    return name, food, quantity, price, delivery_charges