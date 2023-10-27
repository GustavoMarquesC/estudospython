"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)
________________________
|Python|Módulos builtin|
________________________

# Utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
# import random     A unica diferança é na hora de chamar a função

print(random())

from random import randint as rdi, random as rdm


print(rdm())

print(rdi(5, 89))

"""

# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo


from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint())

print(shuffle(['Geek', 'University', 'Python']))

print(randint(3, 7))
