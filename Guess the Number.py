import random
options=list(range(1,101))
print("\t\t\tGuess from 1 to 100\t\t\t\n")
user_score=0
choice=random.choice(options)
chance=10
while chance>0:
    n=int(input("\nGuess the right number:"))
    if(n<choice):
        print(n,"is Too Low")
        chance-=1
        print("You have",chance,"chances left")
    elif(n>choice):
        print(n,"is Too High")
        chance-=1
        print("You have",chance,"chances left")
    else:
        print(n,"is the correct no")
        print("YOU GUESSED RIGHT!!")
        chance=10
        user_score+=1
        print("Score:",user_score)
        choice=random.choice(options)

        
    
