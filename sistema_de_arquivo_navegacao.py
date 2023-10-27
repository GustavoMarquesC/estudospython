"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# Fazer o import

import os

# getcwd() -> pega o current work directory - deritório de trabalho corrente
# Retorna o path caminho absoluto
print(os.getcwd())
# Para mudar o diretório, podemos utilizar o chdir()
os.chdir('..')
print(os.getcwd())
# Fazer o import

import os

# OBS para usuários Windows
# Ter cuidado ao verificar diretórios.
print(os.path.isabs('C:\\Users\\gusta'))

import os

# Podemos identificar o sistema operacional com o módulo os

print(os.name)  # posix (Linux e Mac), nt (Windows)
# Podemos ter mais detalhes no sistema operacional

print(os.uname())
import sys

print(sys.platform)
"""


