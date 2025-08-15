import random

countries = ["USA", "Canada", "Mexico", "Germany", "France"]

populations = {country: random.randint(1, 100) for country in countries}
print(populations)

result = {country: population for (country, population)  in populations.items() if population > 20}
print(result)

text = 'hola, soy juan david'

unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)

