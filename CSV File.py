import csv
with open('c:\pyprg\player.csv','w',newline='')as f:
    w=csv.writer(f)
    n=1
    while(n<=10):
        name=input("Player Name?:")
        score=int(input("Score:"))
        w.writerow([name,score])
        n+=1
print("Player File created")
f.close()
searchname=input("Enter the name to be searched")
f=open('c:\pyprg\player.csv','r')
reader=csv.reader(f)
lst=[]
for row in reader:
    lst.append(row)
q=0
for row in lst:
    if searchname in row:
        print(row)
        q+=1
        if(q==0):
            print("string not found")
f.close()
f.close()
