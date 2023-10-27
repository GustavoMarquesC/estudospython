"""
Funções com Parâmetro Padrão (Default Paramter)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagme de parâmetro seja opcional:
#print('Geek University')
#print()


def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())  #TypeError


def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva à potência informada pelo usuário


# OBS: Se o utilizador passar somente 1 parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado
# deste número
# Se o número passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia.
# Então será calculada esta potência.


#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração;

#Erro:

def teste(potencia, num=2):
    return num ** potencia


#Outros exemplos


def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   # TypeError


#  Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá, {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

#Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretor
- Nos permite trabalhar com exemplos mais legíveis de código

# - Qualquer tipo de dado:
# Números, Strings, Floats, Booleans, Listas, Tuplas, Dicionários, funções e etc.;


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confunsões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável Local
    return f'Oi, {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Olá {prof}'


print(diz_oi())
print(prof)  # NameError

# Atenção com variáveis globais (Se possível, evitar variável global)

total = 0


def incrementa():
    total = total + 1  # A variável não foi inicializada
    return total


print(incrementa())



# Atenção com variáveis globais (Se possível, evitar variável global)

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1  # A variável não foi inicializada
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

"""


