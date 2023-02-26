a=int(input("Enter a number:"))
def  Pal(n):
    s=0
    p=n
    sum=0
    while(n>0):
        r=n%10
        s=s*10+r
        sum=sum+r
        n=int(n/10)
print("Sum of digits is:",sum)
print("Reverse of the number:",s)
    if(p==s):
        print(a,"is palindrome")
    else:
        print(a,"is not palindrome")
Arm(a)