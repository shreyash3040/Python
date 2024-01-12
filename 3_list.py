# lists can contain elements of differenct data types
mixed_list = [1,"shreyash",3.14,True]

# lists can be  sliced  similar to  strings
print(mixed_list[1:2:])

# append - > adds an element to a list

# extend - > appends element of a list to another

print(mixed_list.extend([2]))
print(mixed_list)

# sort is used to sort a list
print([4,32,3,2].sort())

# pop method  (INDEX BASED REMOVAL)
# deletes an element from a list
# if argument given -> deletes that element
# not given -> deletes last element
a = [1,2,3,4,5,6]
print(a.pop())          #o/p - > 6 , it is removed
print(a.pop(0))         #o/p - > 1, index=0 i.e. 1 is removed from the list

# remove   (VALUE BASED REMOVAL)
b = [2,3,43,10,23,3]
print(b.remove(3))
print(b)
# removes first occurance of value=3

# del method
c = [2,32,4,2,1,4,244]
del c[2]            #removes element with index = 2
print(c)

# a list can be made out of tuple
tuple=(1,2,"list",True)
l = list(tuple)
print(l)