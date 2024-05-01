score=int(input("Enter a number: "))

if(score<35):
    print("W grade")

elif(score<55):
    print("C grade")

elif(score<75):
    print("B grade")

elif(score>70 and score<100):  
    print("A grade")

else:
    print("Invalid marks")