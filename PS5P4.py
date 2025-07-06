#Input

tickets = int(input("Enter number of concert tickets"))

#Process
if tickets >= 25:
  price = 50
elif tickets >= 10:
  price = 60
elif tickets >= 5:
  price = 70
else:
  price =75

total = tickets * price

#Output

print(f"quantity: {tickets}")
print(f"price: ${price}")
print(f"total: ${total}")





