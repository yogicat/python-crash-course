# Dictionary is a collection which is unordered, changeable and indexed.
# No duplicate members

person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

print(person, type(person))

# get value
print(person['first_name']) # JS에서 person.first_name
print(person.get('last_name'))


# add key/value
person['phone'] = '123-456-7890'

# get dict keys
# dict_keys(['first_name', 'last_name', 'age', 'phone'])
print(person.keys())

# dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '123-456-7890')])
print(person.items())

# copy dict - JS에서 spread oprator와 비슷
person2 = person.copy()
person2['city'] = 'Barcelona'

print(person, person2)

# remove item
del(person['age'])
person.pop('phone')

# clear - emptying dict
person.clear()

print(person)

# list of dict
people = [
  {'name': 'Dahye', 'age': 30},
  {'name': 'Arya', 'age': 22},
  {'name': 'Brandon', 'age': 30}
]

print(people[1]['name'])
