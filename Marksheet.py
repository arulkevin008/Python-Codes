n=input("Enter your name:")
r=int(input("Enter your roll no:"))
m1=int(input("Enter your language mark:"))
m2=int(input("Enter your English mark:"))
m3=int(input("Enter your Maths mark:"))
m4=int(input("Enter your Physics mark:"))
m5=int(input("Enter your Chemistry mark:"))
m6=int(input("Enter your Computer mark:"))
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35 and m6>=35:
    res="Pass"
else:
    res="Fail"
total=m1+m2+m3+m4+m5+m6
avg=total/6
per=total/600*100
print("Name\t:\t",n)
print("Roll no\t:\t",r)
print("Lang\t:\t",m1)
print("English\t:\t",m2)
print("Math\t:\t",m3)
print("Physics\t:\t",m4)
print("Chem\t:\t",m5)
print("Comp\t:\t",m6)
print("Total\t:\t",total)
print("Average\t:\t",avg)
print("Percent\t:\t",per)
print("Result\t:\t",res)
