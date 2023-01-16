pizzaSize = input("What size of pizza do you prefer? small, medium or Large ")
pepperoni = input("Do you want some pepperoni? ")
xtraCheese = input("Would you like some extra cheese? ")

fee = 0

if pizzaSize == "small":
    fee += 15
elif pizzaSize == "medium":
    fee += 20
else:
    fee += 25

if pepperoni == "yes":
    if pizzaSize == "small":
        fee += 2
    else:
        fee += 3

if xtraCheese == "yes":
    fee += 1

print(f"Your total bill is ${fee}")