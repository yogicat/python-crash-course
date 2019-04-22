x = 10
y = 50

if x > y:
    print(f'{x} is greater than {y}')
elif x < y:
    print(f'{y} is greater than {x}')
else:
    print(f'{y} is equal {x}')

# Membership Operators

numbers = [10, 20, 30, 40]

if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators

# is
if x is y:
    print(x is y)
else:
    print('x is not y')

# is not
if x is not y:
    print(x is not y)

# Loop

people = ['John', 'Paul', 'Sara', 'Susan']

# simple for loop
for person in people:
    print(f'Current person: {person}')

# break
for person in people:
    if person == 'Sara':
        break
    print(f'current person: {person}')

#while

foo = 0
while foo < 10:
    print(foo)
    foo += 1
