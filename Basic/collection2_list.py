a=[1,2,3]

a.append(4)
a.append(5)

a.insert(1,1.5)
a.insert(5,"Four point five")

a[6]="five"
a[4]="four(4)"

a.append("six")#appended string six
a.append(7)#appended 7

a.pop(8)#index 8th element will delete
a.pop()#last element will delete

b=["a","b","d","u","l","b","a","s","i","t","h"]

a.extend(b)
print(a)