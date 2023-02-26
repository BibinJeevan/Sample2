n=int(input("Enter the limit:"))
first=0
second=1
if n<=0:
    print("please enter > 0")
if n>=1:
    print(first)
if n>=2:
    print(second)
    for i in range(1,n-1):
        print(first+second)
        temp=first
        first=second
        second=temp+second
