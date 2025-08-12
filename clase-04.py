set_a = {'Colombia', 'Mexico', 'Bolivia'}
set_b = {'Venezuela', 'Mexico', 'Peru'}

set_c = set_a.union(set_b)
print(set_c)  # Output: {'Colombia', 'Mexico', 'Bolivia', 'Venezuela', 'Peru'}
print(set_a | set_b)  # Output: {'Colombia', 'Mexico', 'Bolivia', 'Venezuela', 'Peru'}

set_d = set_a.intersection(set_b)
print(set_d)  # Output: {'Mexico'}

print(set_a & set_b)  # Output: {'Mexico'}

set_e = set_a.difference(set_b)
print(set_e)  # Output: {'Colombia', 'Bolivia'}

print(set_a - set_b)  # Output: {'Colombia', 'Bolivia'}

set_f = set_a.symmetric_difference(set_b)
print(set_f)  # Output: {'Colombia', 'Bolivia', 'Venezuela', 'Peru'}
print(set_a ^ set_b)  # Output: {'Colombia', 'Bolivia', 'Venezuela', 'Peru'}

