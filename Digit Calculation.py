num=int(input("Enter a number:"))
Sum=0
Product=1
while num>0:
    digit=num%10
    if(digit==0):
        Product=Product*1
    elif(digit>0):
        Product=Product*digit
    Sum=Sum+digit
    num//=10
print(Sum)
print(Product)



