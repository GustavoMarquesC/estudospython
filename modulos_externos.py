"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos em: https://pypi.org

coloramo -> ele é utilizado para permitir impressão de texto coloridos no terminal

# Utilizando o pacote instalado

from colorama import init, Fore, Back

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.MAGENTA + 'Geek University')
print(Back.MAGENTA + 'Geek University')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
