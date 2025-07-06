#APPLIANCE

#INPUT
name = input("What's the name of the appliance? ")
cost = float(input("What's the cost of the appliance? "))

#PROCESS
if cost > 1000:
    warranty = cost * 0.10
else:
   warranty = cost * 0.05

#calcuteing the total price
total = cost + warranty

#OUTPUT
print(f"\nAppliance: {name}")
print(f"Cost: ${cost:}")
print(f"warranty: ${warranty}")
print(f"Total Price (including warranty): ${total}")




