ict=int(input("Enter your ict marks: "))
science=int(input("Enter your science marks: "))
maths=int(input("Enter your maths marks: "))
islam=int(input("Enter your islam marks: "))
sft=int(input("Enter your sft marks: "))


total=(ict+science+maths+islam+sft)
avg=total/5

print("your total is", total)
print("your average is", avg)

if (avg<35):
    print("Additional class is required")
else:
    print("You're good to go!")