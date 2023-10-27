"""
Sorted
OBS: não confunda com a função sort() que já estudamos em listas. O sort() só funciona em listas.
Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome disse, sorte() serve para ordenar.
OBS: o sorted() sempre retorna uma Lista com os elementos do iterável ordenado.
# Exemplo:

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

print(numeros)
numeros = [6, 1, 8, 2]
# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))  # Ordenar do menor para o maior
# Podemos utilizar o sorted() para coisas mais complexas.

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)
# Ordenando por username - Ordem Aldabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32},
]

# Ordena da menor tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menor tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
