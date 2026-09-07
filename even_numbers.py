x=int(input("Enter the number:"))
s=0
c=0
i=1
while(i<=x):
    if i%2==0:
        s=s+i
        c+=1
    i+=1
print("sum of even numbers:",s)
print("number of even numbers:",c)