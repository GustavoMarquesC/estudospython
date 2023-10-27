"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')
print(arquivo.read())

# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica
# onde queremos colocar o cursor.

# Movimentando o curso pelo arquivo com a função seek()


arquivo.seek(22)

print(arquivo.read())

arquivo = open('texto.txt')

# readline() -> função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))
print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o
nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão
. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:
1 - abrir o arquivo;
2 - trabalhar o arquivo;
3 - fechar o arquivo;

# 1 - abrir o arquivo;
arquivo = open('texto.txt')

# 2 - trabalhar o arquivo;
print(arquivo.read())

# 3 - fechar o arquivo;
arquivo.close()

"""

arquivo = open('texto.txt')

print(arquivo.read(50))
