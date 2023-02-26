a=int(input("Enter a number:"))
def  Arm(n):
    s=0
    p=n
    while(n>0):
        r=n%10
        s=s+(r*r*r)
        n=int(n/10)
    if(s==p):
        print(a,"is armstrong")
    else:
        print(a,"is not armstrong")
Arm(a)