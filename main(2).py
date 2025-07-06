# count from 1 to 10 by 1's
# start Value 
#stop value  
# increment value 

for count in range (1, 11, 2):
  print (count)

for number in range(11):
  print(number)

p = float(input("Enter Principle"))
r = float(input("Enter interest rate"))
# header
for count in range (1, 6, ):
  i = p * r
  eb = p + i
  print (count, "   ", p, "  ", eb)
  p = eb