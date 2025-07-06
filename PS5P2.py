#input
part_number = input("Enter part number:")
quantity = int(input("Enter quantity:"))



#process
if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
     unit_cost = 2.00
elif part_number == "80" or part_number == "70":
     unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

#output

print(f"\npart Number: {part_number}")
print(f"unit_Cost: ${unit_cost}")
print(f"total_cost: ${total_cost}")