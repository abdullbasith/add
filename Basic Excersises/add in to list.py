a=[]#list
b=()#tuple
c=list(b)

for i in range(1,6):
    num=int(input("Enter the number: "))
    a.append(num)
    c.append(num)
print("a=",a)
print("c=",c)