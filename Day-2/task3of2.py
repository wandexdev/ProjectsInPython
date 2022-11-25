user_age = input("How old are you? ")
print(user_age)
print()
x = 90 - int(user_age)
x *= 365
y = 90 - int(user_age)
y *= 52
z = 90 - int(user_age)
z *= 12
print(f"days left is {x}, weeks left is {y}, months left is {z}")


