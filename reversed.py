"""
Reversed

OBS: não confunda com a função reverse() que estudamos nas listas.
A função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto (set)
print(set(reversed(lista)))
# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))
# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

