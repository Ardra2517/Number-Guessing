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

    def swapFileData(): 
        file1 = input("enter files name:- ") 
        file2 = input("enter files name:- ") 

        with open(file1, 'r') as a: 
            data_a = a.read() 

        with open(file2, 'r') as b: 
            data_b = b.read() 

        with open(file1, 'w') as a: 
            a.write(data_b) 
    
        with open(file2, 'w') as b: 
            b.write(data_a) 
            
swapFileData() 