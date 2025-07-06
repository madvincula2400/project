#Input
quantity = int(input("Enter quantity of widgets:"))

#Processing
if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
     price = 20
else:
     price = 30

extended_price = quantity * price 
tax =  extended_price * 0.07
total = extended_price + tax 

#Output
print(f"\nYou're buying {quantity} widgets.")
print(f"Price per widget: ${price}")
print(f"extended_price: ${extended_price:}")
print(f"Tax (7%): ${tax:}")
print(f"Total amount due: ${total:}")








