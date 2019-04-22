# collection is ordered and changeable

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'kiwi']

# use a constructor (js에서 new Array와 비슷한..)
numbers2 = list((1, 2, 3, 4, 5))

# get a value
print(fruits[1])  #banana

# length
print(len(fruits))  #3

# append
fruits.append('mango')

# remove
fruits.remove('kiwi')

# insert into position
fruits.insert(2, 'grape')

# change value
fruits[0] = 'cherry'
print(fruits)

# pop
fruits.pop(2)

# reverse
fruits.reverse()

# sort list
fruits.sort()
print(fruits)

# reverse sort
fruits.sort(reverse=True)
print(fruits)
