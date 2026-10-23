import random
options=("planet", "guitar", "window", "python",
    "rocket", "garden", "coffee", "animal", "orange",
    "castle", "school", "jungle", "flower", "market")
word=random.choice(options)
print("\t\t\tGuess the Word\n")
print(options)
n=5
correct_word=""
for i in range(11):
    scrambled_word=input("Guess The Word:")
    if(scrambled_word==word):
        print(word)
        print("You Found Correctly!")
        break
    elif (scrambled_word in word):
        correct_word+=scrambled_word
        print(correct_word)
        print("Good Work")
        print("You have",n,"choice left")
        n-=1 
    elif (scrambled_word not in word):
        print("Nope")
        print("You have",n,"choice left")
        n-=1
