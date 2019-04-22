name = 'Arya'
age = 22

# 1. Concat
# print('hello, my name is '+ name + 'i am ' + age) => age 포매팅 필요

# 2. Arguments by position
print('My name is {name} and age is {age}'.format(name=name, age=age))

# 3. F-Strings (3.6 +)
print(f"My name is {name} and age is {age}")

##### String Methods
s = 'hello world'
s1 = 'python3.6+'
s2 = '0070'

print(s.replace('world', 'you'))

# find position
print(s.find('w'))

# is all numeric => True
print(s2.isnumeric())

# is all alphabetic => False(due to space) , False
print(s.isalpha())
print(s1.isalpha())
