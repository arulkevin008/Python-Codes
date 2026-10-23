import random
options=["rock","paper","scissor"]
print("\t\t\t Rock | Paper | Scissor\t\t\t\n")
user_score=0
com_score=0
while True:
    n=input("Enter your choice:").lower()
    choice=random.choice(options)
    if (n!="rock")and (n!="paper") and (n!="scissor") and (n!="end"):
        print("Invalid input!")
    elif n==choice:
        print("You choose: ",n.capitalize(), "\nComputer choose: ",choice.capitalize())
        print("Draw!")
    elif(n=="paper" and choice=="rock")or \
         (n=="rock" and choice=="scissor")or \
         (n=="scissor" and choice=="paper"):
            print("You choose: ",n.capitalize(), "\nComputer choose: ",choice.capitalize())
            print("You Win!")
            user_score+=1
    elif(n=="end"):
        print("Game Over!!")
        if(user_score>com_score):
            print("Player Wins!")
        elif(user_score<com_score):
            print("Computer Wins!")
        else:
            print("Draw!")
    else:
             print("You choose: ",n.capitalize(), "\nComputer choose: ",choice.capitalize())
             print("Computer Wins!")
             com_score+=1
    print("Your Score:",user_score)
    print("Computer Score:",com_score)
    

