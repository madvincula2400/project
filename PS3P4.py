# Input
make = input("Enter the make of the vehicle: ")
model = input("Enter the model of the vehicle: ")
msrp = float(input("Enter the MSRP amount: $"))
discount_percent = float(input("Enter the discount percent (as a decimal, e.g., 0.15 for 15%): "))

# Processing
amount_off = msrp * discount_percent
discounted_price = msrp - amount_off

# Output
print("\n--- Auto Discount Summary ---")
print(f"Make: {make}")
print(f"Model: {model}")
print(f"MSRP: ${msrp:,.2f}")
print(f"Discount Percent: {discount_percent:.2%}")
print(f"Amount Off: ${amount_off:,.2f}")
print(f"Discounted Price: ${discounted_price:,.2f}")