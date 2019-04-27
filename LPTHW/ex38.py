ten_things = "apples oranges crows telephone light sugar"

stuff = ten_things.split(' ')

more_stuff = [
    "day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"
]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('adding: ', next_one)
    stuff.append(next_one)

print("There we go: ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())

print(' '.join(stuff))
print('#'.join(stuff))
