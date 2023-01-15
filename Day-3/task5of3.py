# Automatic Pizza order Program
print("Yummy Pizza's)
pizzaSize = input("What size of pizza do you prefer? small, medium or Large")
pepperoni = input("Do you want some pepperoni? ")
xtraCheese = input("Would you like some extra cheese? ")
order = 0

if pizzaSize == small:
    order = 15
    print("That would be $15")
        if pepperoni == "yes":
            order +=2
            print(f"Your bill is now{order}")
        else:
            order = order
            print(f"Your bill remains {order}")
                if xtraCheese = "yes":
                    order +=1
                    print(f"Your total bill is {order}")
                else:
                    order = order
                    print(f"Your bill remains {order}")
elif pizzasize == medium:
    order = 20
    print("That would be $20")
        if pepperoni == "yes":
            order +=3
            print(f"Your bill is now{order}")
        else:
            order = order
            print(f"Your bill remains {order}")
                if xtraCheese = "yes":
                    order +=1
                    print(f"Your total bill is {order}")
                else:
                    order = order
                    print(f"Your bill remains {order}")
else:
    print("That would be $25")
        if pepperoni == "yes":
            order +=3
            print(f"Your bill is now{order}")
        else:
            order = order
            print(f"Your bill remains {order}")
                if xtraCheese = "yes":
                    order +=1
                    print(f"Your total bill is {order}")
                else:
                    order = order
                    print(f"Your bill remains {order}")


