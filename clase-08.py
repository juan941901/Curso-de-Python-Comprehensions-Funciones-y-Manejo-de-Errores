def my_print(text):
    print(text * 2)

my_print("Juan ")

def suma(a, b):
    print(a + b)

suma(5, 1)

def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for x in range(min, max):
        sum += x
        return sum

result = sum_with_range(10, 30)
print(result)