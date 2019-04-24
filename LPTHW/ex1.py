# print("Hello World!")
# print("Hello Again")
# print("I like typing this.")
# print("This is fun.")
# print("Yay! Printing.")
# print("I'd much rather you 'not'.")
# # print('I "said" do not touch this.')

# cars = 100
# space_in_a_car = 4
# drivers = 30
# passengers = 90
# cars_driven = drivers
# cars_not_driver = cars - drivers
# carpool_capacity = cars_driven * space_in_a_car
# print("There will be", cars_not_driver, "empty cars today.")
# print(carpool_capacity)

# name = 'oh da'
# age = 30
# height = 166
# eyes = 'dark brown'
# hair = 'black'

# print(f"Let's talk abbout {name}.")
# print(f"He's got {eyes} eyes and {hair} hair.")

# types_of_people = 10
# x = f"There are {types_of_people} types of people"

# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those who {do_not}"

# print(x)
# print(y)

# print(f"I said: {x}")
# print(f"I also said: '{y}'")

# hilarious = False
# joke_evaluation = "Isn't that joke so funny? {}"
# print(joke_evaluation.format(hilarious))

# print("Its fleece was white as {}.".format('snow'))

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))

days = "mon tue wed thu fri sat sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months", months)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("hey \'ho\' \"yo\"")

print('''
I'll do a list
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''')
