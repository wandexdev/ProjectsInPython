print("=== ADVENTURE ISLAND ====")
print()
option1 = input('you are stuck and need to choose between "left" and "right." ').lower()

if option1 == "left":
    option2 = input('oops stuck again, type "sand" or "water" to pass. ')
    if option2 == "sand":
        option3 = input('one of these three women determines your fate. choose between ADE,UGO and Esha. ').lower()
        if option3 == "Eesha":
            print('Yay!!!! you won')
        else:
            print('Game Over Again You loser')
    else:
        print("game overrr")
else: 
    print("Game Over")
