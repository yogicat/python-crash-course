numbers = []

while True:
    number = input("number: ")

    if not number:
        break

    numbers.append(number)

for number in numbers:
    print(number)
