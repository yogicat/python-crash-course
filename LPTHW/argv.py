from sys import argv

# print(len(argv))

# for i in argv:
#     print(i)

x = int(input("x: "))
y = int(input("y: "))
print(f"x is {x}, y is {y}")
x, y = y, x
print(f"x is {x}, y is {y}")
