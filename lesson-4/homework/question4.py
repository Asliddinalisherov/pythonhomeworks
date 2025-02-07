import random

def gamee():
    rannum = random.randint(1,100)
    n = False
    for i in range(10):
        num = int(input())
        if num>rannum:
            print("Too high!")
        elif num<rannum:
            print("Too low!")
        else:
            print("You guessed it right!")
            n = True
            break
    if n == False :
        print("You lost. Want to play again? ")
        decision = input()
        if decision == 'Y' or decision == 'YES' or decision == 'y'or decision == 'yes' or decision == 'ok' :
            gamee()

        

gamee()
        