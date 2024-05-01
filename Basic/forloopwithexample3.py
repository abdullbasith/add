o_count=0
e_count=0

for i in range(1,11):
    if(i%2==0):
        print("even number is ",i)
        e_count=e_count+1
    else:
        print("odd nuumber is ",i)
        o_count=o_count+1
    
print("Odd number count is ",o_count)
print("Even number count is ",e_count)