#Input
quantity = int(input("item quantity:"))

#Process
if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

#output
print(f"you oredered {quantity} items")  
print(f"each item costs: ${unit_price:.2f}")
print(f"Subtotal: ${extended_price:.2f}")
print(f"tax: ${tax:.2f}")
print(f"total: ${total:.2f}")
