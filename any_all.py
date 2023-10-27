"""
Any e All

all() -> Retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([]))  # Todos os números são verdadeiros? True
print(all((0, 1, 2, 3, 4)))  # Todos os números são verdadeiros? True
print(all({0, 1, 2, 3, 4}))  # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))
print(all([letra for letra in 'eiof' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
print(any([0, 1, 2, 3, 4]))  # True
"""