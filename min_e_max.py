"""
Min e Max

Max() retorna o maior valor num iterável ou o maior, de dois ou mais elementos.
# Exemplo

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129

print(max(3, 34))  # 34

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informa o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

Min() retorna o menor valor num iterável ou o maior, de dois ou mais elementos.
val1 = int(input('Informa o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivandar']

print(max(nomes))  # Tim
print(min(nomes))  # Arya

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim
"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio! Como encontrar a música mais tocada e a menor tocada sem usar max(), min() e lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
