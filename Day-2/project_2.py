print("=====Welcome to wande's TIP CALCULATOR=====")
print()
total_bill = input("Give me the total bill ")
print(total_bill)
percent = input("What's the tip rate? 10%, 12% or 15%? ")
print(percent)
total_no = input("How many of you are splitting the bill? ")
print(total_no)

total_result = round((int(percent) + 100) / 100 * int(total_bill), 2)
per_result = total_result / int(total_no)
print(f"Each Person's bill is :{per_result}")

