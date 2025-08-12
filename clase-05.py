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
