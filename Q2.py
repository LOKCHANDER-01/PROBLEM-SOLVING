def calculate_discount(purchase_amount, customer_type):
    # Initial discount based on purchase amount
    if purchase_amount > 2000:
        discount = 0.15  # 15% discount
    elif purchase_amount >= 1000:
        discount = 0.10  # 10% discount
    else:
        discount = 0.0  # No discount

    # Apply the purchase discount
    discount_amount = purchase_amount * discount
    amount_after_discount = purchase_amount - discount_amount

    # Additional discount based on customer type
    if customer_type == "Premium":
        additional_discount = 0.05  # 5% additional discount for Premium members
        additional_discount_amount = amount_after_discount * additional_discount
        final_amount = amount_after_discount - additional_discount_amount
    else:
        additional_discount_amount = 0  # No additional discount for Regular members
        final_amount = amount_after_discount

    # Display results
    print("Original Purchase Amount: $", purchase_amount)
    print("Discount Applied: $", discount_amount)
    print("Additional Discount (if any): $", additional_discount_amount)
    print("Final Payable Amount: $", round(final_amount, 2))


15# Input values
purchase_amount = float(input("Enter the purchase amount: $"))
customer_type = input("Enter the customer type (Premium/Regular): ").capitalize()

# Call the function to calculate and display results
calculate_discount(purchase_amount, customer_type)
