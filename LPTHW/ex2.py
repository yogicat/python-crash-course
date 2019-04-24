# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = int(input()) * 2

# print(f"So, you're {age} old, {height} tall!")

# age = input("How old are you? ")
# height = input("How tall are you? ")

# print(f"So, you're {age} old, {height} tall.")

# from sys import argv
# script, name = argv

# print("The script is called:", script)
# print("The first variable is called:", first)
# print("The second var is called:", second)
# print("The third is called:", third)

# age = input("How old are you? ")
# height = input("How tall are you? ")

# print(f"So, you're {age} old, {height} tall.")

# prompt = 'answer > '

# print(f"Hi {name}, I'm the {script} script.")
# print(f"Do you like me {name}?")
# likes = input(prompt)

# print(f"where do you live {name}?")
# lives = input(prompt)

# print(f"""
# So you said {likes} about liking me.
# You live in {lives}. Tha's cool.
# """)

# txt = open(name)

# print(f"Here's your file {name}")
# print(txt.read())

# txt.close()

# # secondfile = input("type the filename > ")
# # print(secondfile.read())
# # secondfile.close()

# f = open("hello.txt", "w+")

# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))

# f.close()

# print(f"We are going to erase {name}")
# print("hit RETURN")

# input("?")

# target = open(name, 'w+')
# print("truncating the file. goodbye!")
# # target.truncate()

# for i in range(3):
#     line = input("line > ")
#     target.write(f"{line}\n")
#     # target.write("This is line %d\r\n" % line)

# print("good bye")
# target.close()


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"args1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothing")


print_two("bbungti", "Gdol")
print_two_again("Oh", "Gdol")
print_one("bbungti")
print_none()
