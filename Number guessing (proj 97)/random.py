import random 
number=random.randint(1,10)
chance=0

while chance<5:
    guess=int(input("Guess the number"))
    if guess==number:
        print("Congrats!")
        break
    elif guess<number:
        print("Guess higher numbers!")
    else:
        print("Guess lower numbers!")
    
    chance+=1
if not chance<5:
    print("Game Over!")