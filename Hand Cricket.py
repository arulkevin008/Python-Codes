import random
options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_score = 0
com_score = 0
n = input("Enter Batting or Bowling: ").lower()
if n == "batting":
    print("You are Batting!")
elif n == "bowling":
    print("You are Bowling!")
else:
    print("Invalid choice! Defaulting to Batting.")
    n = "batting"
while True:
    try:
        s = int(input("Enter your choice from 1 to 10: "))
        if s < 1 or s > 10:
            print("Invalid Input! Please enter a number between 1 and 10.")
            continue
    except ValueError:
        print("Invalid Input! Please enter a number, not text.")
        continue
    choice = random.choice(options)
    print("Player Choice:", s, "Computer Choice:", choice)
    if s == choice:
        print("OUT!")
        break
    elif n == "batting":
        user_score += s
        print("Your Score:", user_score)
    elif n == "bowling":
        com_score += choice
        print("Computer Score:", com_score)
print("Your Score:", user_score)
print("Computer Score:", com_score)

if(n=="batting"):
    print("You are now bowling")
else:
    print("You are now batting")
while True:
    try:
        s = int(input("Enter your choice from 1 to 10: "))
        if s < 1 or s > 10:
            print("Invalid Input! Please enter a number between 1 and 10.")
            continue
    except ValueError:
        print("Invalid Input! Please enter a number, not text.")
        continue
    choice = random.choice(options)
    print("Player Choice:", s, "Computer Choice:", choice)
    if s == choice:
        print("OUT!")
        break
    elif n == "bowling":
        user_score += s
        print("Your Score:", user_score)
    elif n == "batting":
        com_score += choice
        print("Computer Score:", com_score)
print("Your Score:", user_score)
print("Computer Score:", com_score)
if(user_score>com_score):
    print("\nYOU WON!!!!")
elif (user_score==com_score):
    print("\nDRAW")
else:
    print("COMPUTER WON!!!!")
