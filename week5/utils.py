# Function to calculate the total bill
def calculate_total(coffee, tea, sandwich):
   # Prices of the cafe items
    coffee_price = 8.50
    tea_price = 6.00
    sandwich_price = 12.00

    # Calculate the total cost
    total = (coffee * coffee_price) + (tea * tea_price) + (sandwich * sandwich_price)
    
    # Return the total amount
    return total

# Function to display the receipt
def print_receipt(customer_name, coffee, tea, sandwich, total):
    
    # Print the receipt header
    print("\n===== RECEIPT =====")

    # Display customer information
    print("Customer :", customer_name)

    # Display the quantity of each item
    print("Coffee   :", coffee)
    print("Tea      :", tea)
    print("Sandwich :", sandwich)

    # Print a separator line
    print("-------------------")

    # Display the total bill with 2 decimal places
    print(f"Total = RM {total:.2f}")