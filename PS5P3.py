#INPUT

principal = float(input("enter amount into the cd"))
years = int(input("enter the number of years until maturity"))

#Process
if principal > 100000 and years == 5:
  rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
  rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
  rate = 0.04
else:
  rate = 0.02

interest = principal * rate 

#Output

print(f"\nprincipal: ${principal}")
print(f"interest rate: {rate}%")
print(f"first year interest: ${interest:}")



