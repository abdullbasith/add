n1=int(input("Enter first number"))
n2=int(input("Enter Second number"))
sym=input("Enter what to do")

if(sym=="+"):
    print(n1+n2)
elif(sym=="-"):
    print(n1-n2)
elif(sym=="*"):
    print(n1*n2)
elif(sym=="/"):
    print(n1/n2)
else:
    print("invalid")

