# def my_print(text):
#     print(text * 2)

# my_print("Juan ")

# def suma(a, b):
#     print(a + b)

# suma(5, 1)

# def sum_with_range(min, max):
#     print(min, max)
#     sum = 0
#     for x in range(min, max):
#         sum += x
#         return sum

# result = sum_with_range(10, 30)
# print(result)

"""
Retorno de multiples valores
"""


def find_volume(length=1, width=1, depth=1):
    return length * width * depth

# result = find_volume(10, 20, 3)
result = find_volume()

print(result)