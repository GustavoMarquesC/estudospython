"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe
# arquivos
print(os.path.exists('frutas.txt'))
print(os.path.exists('arquivo.txt'))
# diretório
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('outro'))  # False
print(os.path.exists('geek/university/geek3.py'))  # True
# path absolutos
print(os.path.exists('/home/gusta/guppe'))
print(os.path.exists('home/gusta/Imagens'))

# Criando arquivos
# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste.txt', 'a').close()

# Forma 3

with open('arquivo-teste2.txt', 'w') as arquivo:
    pass

# Criando arquivos

os.mknod('arquivo-teste3.txt')

# Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError
# OBS: Criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError

import os

# Criando diretórios - únicos (um a um)

os.mkdir('templates')
# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

import os

# Criando multi-diretórios

os.makedirs('templates/geek/university')

import os

os.makedirs('templates2/novo2/outro2', exist_ok=True)

import os

# Renomear arquivos e diretórios

os.rename('geek2/novo2', 'geek2')
# OBS: Se o diretório não existir teremos um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

import os

# ATENÇÂO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles não vão para a lixeira.
# Eles somem.

os.remove('geek.txt')
# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

import os

# Removendo diretórios vazios

os.rmdir('templates')
# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError
# OBS: Se o deretório não existir teremos um FileNotFoundError
"""

import os

# Removendo todo o conteúdo do diretório

