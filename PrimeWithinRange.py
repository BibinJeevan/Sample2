x=int(input("Enter 1st limit:"))
y=int(input("Enter 2nd limit:"))
while(x<y):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        print(x)
    x=x+1
