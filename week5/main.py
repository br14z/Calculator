# Import the functions from utils.py
from utils import calculate_total, print_receipt

# Get the customer's name
customer_name = input("Customer name: ")

# Get the quantity of each item
coffee = int(input("Coffee quantity: "))
tea = int(input("Tea quantity: "))
sandwich = int(input("Sandwich quantity: "))

# Calculate the total bill
total = calculate_total(coffee, tea, sandwich)

# Print the customer's receipt
print_receipt(customer_name, coffee, tea, sandwich, total)