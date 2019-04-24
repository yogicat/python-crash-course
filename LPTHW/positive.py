def main():
    i = get_positive_int("positive integer: ")
    print(i)


def get_positive_int(prompt):
    while True:
        n = int(input(prompt))
        if n > 0:
            return n


main()
