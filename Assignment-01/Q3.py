# Online Shopping Discount Eligibility
order_amount = float(input("Enter order amount: ₹"))
membership = input("Are you a member? (yes/no): ").strip().lower()#strip for removing leading and starting spaces and lower for converting to lowercase

# Validate the order amount
if order_amount < 0 or order_amount > 100000:
    print("Invalid order amount.")
    print("Eligibility Status: Not Eligible")

elif membership != "yes" and membership != "no":
    print("Invalid membership status. Enter yes or no.")

else:
    discount_percentage = 0

    if order_amount >= 5000:
        discount_percentage = 15
    elif membership == "yes" and order_amount >= 2000:
        discount_percentage = 10

    discount_amount = order_amount * discount_percentage / 100
    final_amount = order_amount - discount_amount

    print("Original Amount: ₹", order_amount)
    print("Discount Percentage:", discount_percentage, "%")
    print("Discount Amount: ₹", discount_amount)
    print("Final Payable Amount: ₹", final_amount)

    if discount_percentage > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: No discount")
