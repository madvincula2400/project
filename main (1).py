
#for c in range (1, 6, 1):
#  print (c)
#  for count in range (1, 11, 1):
#   print (count)

p = float(input("Enter principle amount"))
t = int(input("Enter term in years"))
r = float(input("Enter interest rate in decimal form"))

for y in range (1,t+1,1):
  i = p * r
  nb = i + p
  print ("Year:  ", y)
  print ("Starting Amount: ", p)
  print ("Interest earned:", i)
  print ("End of year balance: ", nb)
  p = nb
