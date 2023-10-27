"""
tupla = (1, 2, 3)

print(tupla[1])

"""

from collections import namedtuple

#  Precisamos definir o nome e paramêtro

#  Forma 1 - declaração

cachorro = namedtuple('cachorro', 'idade raca nome')

#  Forma 2 - declaração

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#  Forma 3 - declaração

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#  Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

#  Forma 1

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

#  Forma 2

print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
