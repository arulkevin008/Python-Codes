print("\t\t\tGuess the number by clue\t\t\t")
import random
options = list(range(1, 101))
choice = random.choice(options)
n=5
while n>0:
    if 1 <= choice <= 25:
            print("The number is between 1 and 25.")
    elif 26 <= choice <= 50:
            print("The number is between 26 and 50.")
    elif 51 <= choice <= 75:
            print("The number is between 51 and 75.")
    else:
            print("The number is between 76 and 100.")

    if choice % 2 == 0:
            print("It is even.")
    elif choice % 2 == 1:
            print("It is odd.")
        
    if choice % 5 == 0:
            print("It is divisible by 5.")
    if choice % 3 == 0:
            print("It is divisible by 3.")
    if choice % 3 != 0 and choice % 5 != 0:
            print("It is not divisible by 3 or 5.")

    num = int(input("Enter the number: "))
    
        
    if num == choice:
        print("You guessed correctly!!")
        break
    else:
        print("Wrong guess. Try again.")
        n-=1
        print("You have",n,"chances left")
    
