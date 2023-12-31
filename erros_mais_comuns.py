"""
Erros mais comuns em Python
É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código

Os erros mais comuns
1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escrever algo que o Python não
reconhece como parte da linguagem

Exemplos SintaxError
a)
def funcao:
    print('Geek University')
b)
None = 1
c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.
Exemplos NameError
a) print(geek)

b) geek()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError

a)
print(len(5))
b)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índece inválido

Exemplos de IndexError

a)
lista = ['Geek']
print(lista[2])
b) lista = ['Geek]
print(lista[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor
inapropriado.

Exemplos ValueError

a)print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

Exemplos KeyError

a)
dic = {}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 Espaços)

Exemplos IndentationError

a)
def nova():
print('Geek')
b)
for i in range(10):
i + 1
"""


