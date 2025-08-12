set_countries = {'Colombia', 'Mexico', 'Bolivia'}

print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5}
print(set_numbers)

set_types = {1, False, 'Hola mundo', 3.14}
print(set_types)

set_from_string = set("Hola") # Esto crea un conjunto a partir de uno de los caracteres de la cadena
print(set_from_string)

set_from_tuples = set(('abc', 'abc', 'def', 'as')) # Esto crea un conjunto a partir de una tupla
print(set_from_tuples)

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set_from_list = set(numbers)
print(set_from_list)

unique_numbers = list(set_from_list) # Convertimos el conjunto de nuevo a lista, con los números unicos sin repetir
print(unique_numbers)

