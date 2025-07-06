#PS4P5

#INPUT
last_name = input("Enter your last name:")
dependents = int(input("Enter number of dependents:"))
gross_income = float(input("Enter the gross income"))


#PROCESSING

adjusted_income = gross_income - (dependents * 12000)


if adjusted_income >50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = adjusted_income * tax_rate

#MAKING SURE

if income_tax < 0:
    income_tax = 100.00

#OUTPUT
print(f"\nName: {last_name}")
print(f"gross income: ${gross_income:}")
print(f"number of dependents: {dependents}")
print(f"Adjusted gross income: ${adjusted_income:}")
print(f"income tax owed: ${income_tax:}")















