bs=int(input("Enter the basic salary of an employee:"))
if(bs<25000):
    da=bs*80/100
    hra=bs*20/100
elif(bs>=25000 and bs<40000):
    da=bs*90/100
    hra=bs*25/100
elif(bs>=40000):
    da=bs*95/100
    hra=bs*30/100
gs=bs+hra+da
print("---------------------GROSS SALARY-------------------------")
print("Basic Salary:",bs)
print("Dearness Allowance:",da)
print("House Rent Allowance:",hra)
print("Gross Salary:",gs)
print("----------------------------------------------------------")
      
