A = {1,3,4}
B = {3,4,5}

A.add(5)        #adds element to A
print(A)        #{1, 3, 4, 5}

A.remove(3)     #removes elements from A
print(A)        #{1, 4, 5}

print(A.union(B))       #union of two sets
print(A|B)              #union of two sets
print(A-B)              #intersection of two sets
print(A==B)             #checks equivalence
print(A>=B)             #checks if subset
print(A ^ B)

print(1 in A)           #checks if element=1 is present in set A

