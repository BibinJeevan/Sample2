a=input("enter the string:")
l=list(a)
for i in l:
    c=0
    if i!="":
        for j in range(0,len(l)):
            if i==l[j]:
                c=c+1
                l[j]=""
        print(i,"=",c)
