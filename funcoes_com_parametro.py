"""
Função com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;
Se pensarmos num programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se pensarmos numa função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

#Refatorando uma função


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

#  print(quadrado())  #  TypeError


#  Refatorando a função


#def cantar_parabens(aniversariante):
#print('Parabéns pra você')
#print('Nesta data querida')
#print('Muitas felicidas')
#print('Muitos anos de vida')
#print(f'Viva o/a {aniversariante}')


cantar_parabens('Patricia')

#Funções podem ter 'N' parâmetros de entrada. Ou seja, podemos receber como entrada numa função quantos parâmetros forem
#necessários. Eles são separados por vírgula.

#Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))


#  OBS: Se informarmos um número errado de parâmetro ou argumentos, teremos TypeError

#  print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
#  print(soma(4))  # TypeError - Passando argumentos a menos

# Nomeando parêmtros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', "Jolie"))


#  A diferença entre Parâmentros e Argumentos

#  Parâmetros são variáveis declaradas na definição de uma função;
#  Argumento são dados passados durante a execucão de uma função;

#  A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))


#  Argumentos nomeados (keyword Arguments)

#  Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem;

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Gustavo'))


"""


#  Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
else:
    print('O módulo funcoes_com_parametro.py foi importado')
