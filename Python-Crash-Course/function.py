# no curly brackets


# create function
def sayHello(name='Sam'):
    print(f"hello {name}")


sayHello("Dahye")
sayHello()


# Return values
def getSum(a, b):
    total = a + b
    return total


num = getSum(3, 4)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions.

getSub = lambda num1, num2: num1 - num2
print(getSub(100, 20))
