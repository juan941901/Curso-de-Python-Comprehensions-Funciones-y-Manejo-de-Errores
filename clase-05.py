numbers = []

for element in range(1, 11):
    numbers.append(element)

print(numbers)

"""
Esta es una lista de números del 1 al 10.
escrita de manera tradicional
"""

# List comprehension
numbers = [element for element in range(1, 11)]
print(numbers)

numbers = [element * 2 for element in range(1, 11)]
print(numbers)

# List comprehension con condicion

# Forma tradicional
numbers = []

for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element)

print(numbers)

# Forma de comprension de listas
numbers = [element for element in range(1, 11) if element % 2 == 0]
print(numbers)
