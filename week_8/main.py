# Import the function that collects customer information
from customer import get_customer

# Import the function that prints the receipt
from receipt import print_receipt


# Main function controls the program
def main():

    # Get the customer's information from customer.py
    name, food, quantity, price, delivery_charges = get_customer()

    # Send the information to receipt.py to print the receipt
    print_receipt(
        name,
        food,
        quantity,
        price,
        delivery_charges
    )


# Run the main function only when this file is executed directly
if __name__ == "__main__":
    main()