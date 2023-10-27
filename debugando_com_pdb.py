"""
Debuggando com PDB
PDB -> Python Debugger

bug -> inseto

# OBS: a utilização do print() para debugar é uma prática ruim


def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB
# Exemplo com o PyCharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Exemplo com o PDB

# Para utilizar o PDB, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comando básicos do PDB
# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por queê utilizar este formato?
# O degug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas no início do file
# por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente onde vamos debuggar, e ao
# finalizar já fazemos a remoção

# Exemplo com o PDB

# Para utilizar o PDB, precisamos importar a biblioteca pdb e então utilizar a função set_trace()
# *A partir do Python3.7 não é mais necessário importar a biblioteca pdb, pois a comando de debug foi incorporado como
# função built-in (integrada) chamada breakpoint()

# Comando básicos do PDB
# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# OBS: Cuidado com conflitos entre nomes de variável e os comando do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes da variáveis são os mesmos dos comando do pdb, devemos utilizar o comando p para imprimir as variáveis
# ou seja: p nome_da_variavel
