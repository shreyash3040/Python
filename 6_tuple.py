# To generate a tuple with single element,
# add a comma after that element
# otherwise a tuple wont be created

tuple = ("geeks")
print(type(tuple))      #<class 'str'>

tuple = ("geeks",)      #<class 'tuple'>
print(type(tuple))

# tuples are immutable in nature
# once created cant be changed
# 1. cant be appendec,extended
tuple = (1,2,3,4,4)
# 2. cant remove any element
# 3. cant change the elements in tuple
# tuple[2]=10      #TypeError: 'tuple' object does not support item assignment

#But we can find items in a tuple,
# since it does not change the tuple
# print(tuple[100])       #IndexError: tuple index out of range
print(tuple[-1])
print(tuple[2])

del tuple       #tuple can be deleted using del keyword

# Tuples support slicing same as list
tuple = (1,2,"gfg",True)
print(tuple[::-1])
del tuple

# Converting a list into tuple
list = [1,2,3,4,"hey",True]
tup = tuple(list)
print(tup)