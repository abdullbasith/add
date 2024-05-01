sum=0
c=[]
for i in range(1,8):
    x=int(input("Enter " +str(i)+ " number: "))
    c.append(x)

print("The first "+str(i)+" Number is: ",c)

for x in c:
    sum=sum+x
print("The total is ", sum)