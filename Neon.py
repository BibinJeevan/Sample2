a=int(input("Enter a number:"))
def Neon(n):
    s=0
    p=n
    q=n*n
    while(q>0):
        r=q%10
        s=s+r
        q=int(q/10)
    if(s==p):
        print(a,"is neon")
    else:
        print(a,"is not neon")
Neon(a)
