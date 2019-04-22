x = 1  # int
y = 2.5  #float
name = 'Dahye'  # str
is_cool = True  # bool

# multiple assignment
# 자바스크립트의 destructuring 비슷하다.
a, b, friend, is_here = (2, 4.2, 'John', True)

foo = a + b
# type(foo) => <class 'float'>

# 타입 체크
print(type(foo))

# Casting
a = str(a)
b = int(b)
# 4.2 => 2

print(f"type of a is {type(a)}, value of b is {b}")
