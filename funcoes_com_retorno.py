"""
Função com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno dde print: {ret_pr}')

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None
OBS: Função Python que retornam valor, devem retornar ester valores com a palavra reservada return
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
da função para outras funções.

#  Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7()}')


#  Refatorando a primeira função

def diz_oi():
    return 'Oi, '


alguem = 'Pedro!'

print(diz_oi() + alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, numa função, diferenter returns;
#Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)
print(type(outra_funcao()))

3 - Podemos, numa função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

#  Exemplo 1


def diz_oi():
    #  print('Estou sendo executado antes do retorno... ')
    return 'Oi, '
    #  print('#Estou sendo executado após do retorno... ')


print(diz_oi())

#  Exemplo 2


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

#  Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    #  Gera um número pseudoaleatório entre 0 e 1
    if random > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""


#  Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
