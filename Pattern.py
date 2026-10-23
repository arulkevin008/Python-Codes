rows = int(input("Enter the no of rows:"))
for i in range(1, rows+1):
    print("@"*i)
print("\n")
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j,end = " ")
    print()
print("\n")
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
print("\n")
for i in range(1, rows+ 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()
print("\n")
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" " * j)
    print()
print("\n")
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j,"#",end = " ")
    print()

    
