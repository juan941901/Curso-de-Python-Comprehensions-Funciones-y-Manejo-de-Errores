set_countries = {'Colombia', 'Mexico', 'Bolivia'}

size = len(set_countries)
print(size)

print('Colombia' in set_countries)
print('Peru' in set_countries)

set_countries.add('Peru')
print(set_countries)

set_countries.update({'Peru', 'Argentina', 'Chile'})
print(set_countries)

set_countries.remove('Peru')
print(set_countries)

set_countries.discard('Venezuela')
print(set_countries)

set_countries.clear()
print(set_countries)