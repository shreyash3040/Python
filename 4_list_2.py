#INSERT METHOD
# takes two arguments position,value

list = [3,1,20,14]
list.insert(0,100)      #adds element at index 0
print(list)

tuple = (1,"shreyash")
list.insert(1,tuple)    #inserts tuple at index 1
print(list)             #[100, (1, 'shreyash'), 3, 1, 20, 14]


list1= [1,2,3]
list2= [4,5,6]
list = list1+list2
print(list)

#we can also add a set to python
set = {1,2}
list.insert(1,set)
print(list)