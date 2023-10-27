"""
Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])

# Com generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nomes[0] == 'C' for nome in nomes)
print(type(res))
print(res)

from sys import getsizeof

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(24989249284))
print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de número com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
# Gerando uma lista de número com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
# Gerando uma lista de número com Dictionary Comprehension
dic_comp = getsizeof({x * 10 for x in range(1000)})
# Gerando uma lista de número com Generator
gen = getsizeof(x * 10 for x in range(1000))
print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehesion: {list_comp}')
print(f'Set Comprehesion: {set_comp}')
print(f'Dictionary Comprehesion: {dic_comp}')
print(f'Generator Expression: {gen}')
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
