"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, faz referência á Teoria dos Conjuntos da Matemática.

- Aqui no Python, os conjuntos são chamados de 'Sets'.

- 'Sets' (conjuntos) não possuem valores duplicados;
- 'Sets' (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os Conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos ('Set') e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

#  Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  #  Repare que temos valores repetidos.

print(s)
print(type(s))

#  OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error e não
#  fará parte do conjunto.

#  Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

#  Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

#  Além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#  Listas e tuplas aceitam valores duplicados, já o dicionário não aceita CHAVES duplicadas e o conjunto não aceita
#  valores duplicados

#  Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}

print(s)
print(type(s))

#  Podemos iterar em um set normalmente
for valor in s:
    print(valor)

#  Usos interessantes com sets

#  Imagine que fizemos um formulário de cadastro de visitantes em um feira ou museu e os visitantes informam manualmente
#  a cidade de onde vieram.

#  Nós adicionamos cada cidade em um lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['Bela Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

#  Agora precisamos saber quantas cidade distintas, ou seja, única, temos.

#  O que fazer?

#  Podemos utilizar o set para isso:

print(len(set(cidades)))

#  Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
print(s)

#  Removes elementos em um conjunto
s = {1, 2, 3}
print(s)

#  Forma 1

s.remove(3)

print(s)

#  Forma 2

s.discard(2)

print(s)

#  Veja que alguns alunos que estudam Python também estudam Java.

#  Precisamos gerar um conjunto com nomes de estudantes únicos

#  Forma 1 - Utilizando union

unicos1= estudantes_python.union(estudantes_java)
print(unicos1)

#  Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

#  Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)

print(ambos1)


#  Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

#  Métodos Matemáticos de Conjuntos

#  Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

