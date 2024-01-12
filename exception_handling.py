a = 5
b = 2

try:
    print("resource opened")
    print(a/b)
    k=int(input("Enter a number"))

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

finally:
    print("resource closed")
