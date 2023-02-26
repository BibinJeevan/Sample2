a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no:"))
c=int(input("Enter 3rd no:"))
s=0
def Sum(a,b,c):
    if(a==b==c):
        return(a*3)
    else:
        return(a+b+c)
print("Sum=",Sum(a,b,c))
