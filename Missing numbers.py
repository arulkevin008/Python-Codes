import random

List=list(range(1,101))
rand_num=random.choice(List)
List.remove(rand_num)
print(List)
num=int(input("Enter the missing number:"))
if (num<101 and num not in List):
    print(f"{num} is correct")
elif(num in List):
    print(f"{num} is incorrect")
elif(num>100):
    print("Value from 1 to 100 only")
else:
    print("Invalid Input")

