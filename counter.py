"""

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

#  Utilizando o Counter

res = Counter(lista)

print(type(res))

print(res)

#  Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

#  Para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrência.

#  Exemplo 2

from collections import Counter

print(Counter('Geek University'))

#  Exemplo 3


from collections import Counter

texto = Exemplo de texto

palavras = texto.split()

print(palavras)

res = Counter(palavras)

print(res)

#  Encontrando as 5 palavras com mais ocorrência no texto.
print(res.most_common(5))

"""

