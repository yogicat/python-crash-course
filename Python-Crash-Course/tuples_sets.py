# Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.
# create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# create using constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# 1개짜리 tuple 에는 trailing comma 필요
fruits2 = ('Apples', )

print(fruits, fruits2)

# Can't change value
# 'tuple' object does not support item assignment
# fruits[0] = 'Banana'  # 에러!

# delete tuple
del fruits2

# print(fruits2)

#### SET
# Set is a collection which is unordered and unindexed.
# No duplicate members.

vege_set = {'Basil', 'Carrot', 'Eggplant'}

# check if in set
print('Kale' in vege_set)  # False

# add to set
vege_set.add('Kale')

# add duplicate - 중복으로 추가되지 않는다.
vege_set.add('Basil')
print(vege_set)

# remove from set
vege_set.remove('Carrot')
print(vege_set)

# clear set
# vege_set.clear()
# print(vege_set)

# Delete
# del vege_set
