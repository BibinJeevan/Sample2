l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1)
print(l2)
def list(l1,l2):
    for i in l1:
        for j in l2:
            if(i==j):
                return("true")
if(list(l1,l2)=="true"):
    print("common value occurs")
else:
    print("no common value")
