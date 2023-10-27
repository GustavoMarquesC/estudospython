"""
Módulos Customizados

Como módulo Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste curso são módulos
Python prontos para sem usados.

# Importando uma função específica do nosso módulo
from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
