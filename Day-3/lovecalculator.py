# Automating love score process
print()
firstname = input("give me your preferred name")
secondname = input("give me your partners name")
joinName = firstname + secondname
small_joinName = joinName.lower()

t = small_joinName.count("t")
r = small_joinName.count("r")
u = small_joinName.count("u")
e = small_joinName.count("e")
true = t+r+u+e
l = small_joinName.count("l")
o = small_joinName.count("o")
v = small_joinName.count("v")
e = small_joinName.count("e")
love = l+o+v+e

score = str(true) + str(love)

if score < 10 or score > 90:
    print(f"your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print (f"youre score is {}, you are alright together")    
       