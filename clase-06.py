# Forma tradicional

dict = {}

for i in range(1, 6):
    dict[i] = i * 2

print(dict)

# Forma de comprension de diccionarios

dict = {i: i * 2 for i in range(1, 6)}
print(dict)

# Creación del diccionario a partir de una lista

import random

countries = ["USA", "Canada", "Mexico", "Germany", "France"]
population = {}

for country in countries:
    population[country] = random.randint(1, 100)

print(population)


population = {country: random.randint(1, 100) for country in countries}
print(population)

# Union de listas

names = ['juan', 'camila', 'elizabeth']
ages = [31, 29, 1]

print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)

