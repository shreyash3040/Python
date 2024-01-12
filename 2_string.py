# str = "shreyash bhatale"
# print(str[::-1])
#

str = "shreyash bhatale"
str = "".join(reversed(str))
print(str)

# join method is a string method that concatenates elements of
# an iterable into a single string.
# this method returns a single  string
# seperator.join(List)

ls = ['1','2','3']
seperator="_"

print(seperator.join(ls))

# counts the number of occurances of a substring in a string
print("shreyash".count("s"))

# returns True/False if endswith given substring
print("shreyahs".endswith("ahs"))

# returns the lowest index of substring if it is found
# if not found returns -1
print("shreyash".find("a"))

print("i am shreyash".split(" "))
