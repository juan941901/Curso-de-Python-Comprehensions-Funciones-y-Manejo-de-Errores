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