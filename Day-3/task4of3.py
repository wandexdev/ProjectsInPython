# leap yearrr
year = int(input("type in the year to check"))
byfour = int(year % 4)
byhundred = int(year % 100)
byfourhun = int(year % 400)

if byfour != 0:
    print("Its not a leap year")
elif byhundred != 0:
    print("its a leap year!")
elif byfourhun == 0:
    print("its a leap year!")
else:
    print("its not a leap year!")

