price = 100 #Global

def local_scope():
    price = 200 #Local
    return price

print(price)
result = local_scope()
print(result)