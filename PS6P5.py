total_discounts = 0


answer = input("Do you want to use this program? (Yes to continue): ")

while answer == "Yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: $"))

    extended_price = quantity * price

    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print("Extended Price: $" + str(round(extended_price, 2)))
    print("Discount Amount: $" + str(round(discount_amount, 2)))
    print("Total: $" + str(round(total, 2)))

    total_discounts = total_discounts + discount_amount

    answer = input("Do you want to enter another order? (Yes to continue): ")

print()
print("Final Results:")
print("Total of all discounts: $" + str(round(total_discounts, 2)))