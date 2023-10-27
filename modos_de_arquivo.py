"""
Modos de abertura de arquivos

r -> abre para leitura - padrão
w -> abre para escrita - sobrescreve caso o arquivo já exista
x -> abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError
a -> abre para escrita, adicionando o conteúdo ao final do arquivo.
#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo será adicionado
ao final do arquivi SEMPRE. (Não é possível utilizar a função seek().

http://docs.python.org/3/library/functions.html#open

# Exemplo 'x'
try:
    with open('university.txt', mode='x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe.')

Exemplo 'a':

    with open('frutas.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

#Exemplo 'r+'
with open('outro.txt', 'r+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('Testando!\n')
    arquivo.write('A.\n')
    arquivo.write('Novamente.\n')

"""


