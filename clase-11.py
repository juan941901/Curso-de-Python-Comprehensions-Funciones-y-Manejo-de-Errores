increment = lambda x : x + 1

result = increment(5)

print(result)

full_name = lambda name, last_name : f"the full name is {name.title()} {last_name.title()}"

text = full_name("JUAN", "CORDOBA")
print(text)


def aplicar_operacion(x, operacion):
    return operacion(x)

print(aplicar_operacion(5, lambda n: n ** 3))

def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

por_2 = multiplicador(2)
print(por_2(5))  # 10

def increment(x):
  return x + 1

increment_v2 = lambda x: x +1

def high_ord_func(x, func):
  return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ord_func_v2(2, increment_v2)
print(result)
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)