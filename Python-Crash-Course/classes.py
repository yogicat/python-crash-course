# class is like a blueprint for creating objects.
# almost everything in python is an object


# create class
class User:
    # Constructor
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def greeting(self):
        return f'My name is {self.name} from {self.city} and I am {self.age} years old.'

    def has_birthday(self):
        self.age += 1


# init user object
brad = User('Brad Pitt', 'Seoul', 30)

print(type(brad), brad.name)  # <class '__main__.User'>

print(brad.greeting())

brad.has_birthday()

print(brad.greeting())

# extend class


class Customer(User):
    #constructor
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance += balance


janet = Customer('Janet Johnson', 'New York', 25)

janet.set_balance(100)

print(janet.balance)
