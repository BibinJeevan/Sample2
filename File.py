import filecmp
a=open("file.txt","r")
s=a.read()
print(S)

b=open("file2.txt","w")
t=b.write(s)
b.close
c=filecmp.cmp("file1.txt","file2.txt")
print(c)
