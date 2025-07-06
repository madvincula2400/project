

print("Welcome to Kram's coffee haus") 

name = input("What is your name?\n")

print("Hello " + name + ", thank you for  coming in today.\n\n\n")

menu = "Latte, Mocha, Espresso, Cappuccino"

print(name + ", what would you like from our menu? Here is what we are serving. \n"
      + menu)

order = input()

price = 3

quantity = input("How many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))


print("Sounds good " + name + ", we'll have your " + quantity +" "+ order + 
"\nready for you in a few minutes.\n")




























