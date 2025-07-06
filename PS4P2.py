#item price


item = input("Enter item (A or B): ")
quantity = int(input("Enter quantity:"))

if item == "A":
  unit_price = 10.00
else:
  unit_price = 20.00
extended_price = quantity * unit_price

print(f"Item: {item}")
print(f"Unite Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")






