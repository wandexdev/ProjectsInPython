#BMI is weight divide (square of height)

weight = input("give me your weight in kg ")
height = input("give me your height in m ")

BMI = float(weight) / float(height) ** 2
print(type(BMI))
print(BMI)

Integer_BMI = int(BMI)
print(type(Integer_BMI))
print(Integer_BMI)
