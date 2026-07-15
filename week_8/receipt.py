# This function calculates and prints the customer's receipt
def print_receipt(name, food, quantity, price, delivery_charges):

    # Calculate the price before extra charges
    subtotal = quantity * price

    # Calculate a 5% service charge
    service_charge = subtotal * 0.05

    # Calculate the final amount
    grand_total = subtotal + service_charge + delivery_charges

    # Display the receipt
    print("\n========== RECEIPT ==========")

    # Display the customer's order information
    print(f"Customer : {name}")
    print(f"Food     : {food}")
    print(f"Quantity : {quantity}")
    print(f"Price    : RM {price:.2f}")

    # Print a separator line
    print("-----------------------------")

    # Display all payment calculations
    print(f"Subtotal             : RM {subtotal:.2f}")
    print(f"Service Charge (5%)  : RM {service_charge:.2f}")
    print(f"Delivery Charge      : RM {delivery_charges:.2f}")

    # Print another separator line
    print("-----------------------------")

    # Display the final total
    print(f"TOTAL                : RM {grand_total:.2f}")

    # End the receipt
    print("=============================")