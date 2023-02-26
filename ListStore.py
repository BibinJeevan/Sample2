li=[1,3,4,5,6,7,8,9,10,15]
print("list=",li)
for i in li:
    if(i%3==0 and i%5==0):
        print("c")
    elif(i%3==0):
        print("a")
    elif(i%5==0):
        print("b")
    else:
        print(i)
        
