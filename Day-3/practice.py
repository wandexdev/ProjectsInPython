# Practicing mulpile if's in one program

print('practice')
height = int(input('whats ur height in cm? '))
fee = 0
if height > 120:
    print('yes ride')
    age = int(input('how old are you? '))
    if age < 10:
        fee = 10
        print("your fee is $10")
    elif age <= 18:
        fee = 18
        print("your fee is $18")
    else:
        fee = 25
        print("your fee is $25")

    photo = input("Do you want your photo taken? ")
    if photo == "yes":
        fee = fee + 3
        print(f"your new fee is ${fee}")
    else:
        fee = fee
        print(f"your new fee is ${fee}")
else:
    print('No ride')

