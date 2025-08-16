increment = lambda x : x + 1

result = increment(5)

print(result)

def aplicar_operacion(x, operacion):
    return operacion(x)

print(aplicar_operacion(5, lambda n: n ** 3)) 

full_name = lambda name, last_name : f"the full name is {name.title()} {last_name.title()}"

text = full_name("JUAN", "CORDOBA")
print(text)