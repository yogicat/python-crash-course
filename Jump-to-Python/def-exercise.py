# def add_mul(choice, *args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result += i

#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result *= i
#     return result

# print(add_mul('add', 1, 2, 3, 4))
# print(add_mul('mul', 1, 2, 3, 4))

# ---------------------------------- #

# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(name='dahye', last='oh')
# # 인자로 넘겨진 값이 dict으로 만들어진다.

# def add_and_mul(a, b):
#     return a + b, a * b

# # (16, 48) 튜플을 반환한다.

# print(add_and_mul(4, 12))

# ---------------------------------- #

# def say_myself(name, old, man=True):
#     print(f"my name is {name}")
#     print(f"I am {old} years old")

#     if man:
#         print("I am a man")
#     else:
#         print("I am not a man")

# say_myself('David', 30)
# say_myself('Alex', 20, False)

# ---------------------------------- #

# a = 1

# def var_test(a):
#     a = a + 1
#     print(f"a inside def is {a}")  # a is a

# var_test(a)
# print(a)  # a is 1

# 변수는 함수 스코프를 가진다. 함수안에서 밖의 변수를 가져오려면 global을 붙인다.

# ---------------------------------- #

# b = 2

# def test(a):
#     global b
#     b += a  # 밖에 있는 변수 b에 a값을 더한다.

# test(2)
# print(b)    # b값이 변한것 확인

# ---------------------------------- #

# b = 2
# def test(b):
#     b = b + 1
#     return b  # 1을 더한 후 반환한다.

# b = test(b)  # 반환한 값을 재할당
# print(b)

# ---------------------------------- #

# 람다

add = lambda a, b: a + b
result = add(3, 4)
print(result)
