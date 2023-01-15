weight = float(input("what is your weight in kg? "))
height = float(input("what is your height in m? "))
BMI = weight / (height ** 2)

if BMI < 18.5:
    print("youre underweight")
elif BMI < 25:
    print("you have a normal weight")
elif BMI < 30:
    print("youre overweight")
elif BMI < 35:
    print("youre obese")
else:
    print("youre clinically obese")

