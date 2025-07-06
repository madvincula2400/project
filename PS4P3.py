#PS4P3
#Input
books = int(input("How many books have are you ordering? "))
cost_per_book = float(input("Enter the cost per book: "))

order_total = books * cost_per_book

#Process
if order_total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00

final_total = order_total + shipping


#Output
print(f"\nBooks ordered:")
print(f"Order Total (before shipping): ${order_total:}")
print(f"Shipping Charge: ${shipping:}")
print(f"Total Amount Due: ${final_total}:")




