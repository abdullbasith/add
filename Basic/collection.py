#List[]
a=[1,2,3]
b=["a","b","c"]
#print(type(a))
a.append(1)
a.append(2)
a.append(3)
a.append("ab")#append
a.insert(1,"abi")#insert
a[4]=25#modify
a.pop(7)#Remove
a.pop()#last element will deleted
a.extend(b)#another list will merged to current list
#print(a)

#Tuple()(we can not modify(add or remove))

x=("ab","cd","ef",1,2,3,4,5,6)
print(type(x))

#we can cast the tuple. for ex: int--->str , str--->int

z=list(x)#casting
print(z)
z.pop(0)
print(z)

print(x)

print()

#Set{} (can't input duplicate values(can but not printable))
f={1,2,3,4,5}
print(type(f))
print()
print(f)
print()
f.add(10)
print(f)
f.add("ac")
print(f)
f.remove(3)#3 Will remove.
print(f)
f.pop()#Random value will poped.when we run the program.the set will unordered.
print(f)
f.update("a")
print(f)
f.update("shaka")
print(f)
f.update("Abdul basth")
print(f)
#we can't modify sets like a[0]=10,but we can add or remove values