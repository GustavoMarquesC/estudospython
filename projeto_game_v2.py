import random
from typing import Tuple
LISTA_OPERADORES = ['+', '-', '*']


def nivel_dificuldade(dificuldade: int) -> Tuple:

    operador_aleatorio = random.choice(LISTA_OPERADORES)

    if dificuldade == 1:
        numero1: int = random.randint(0, 9)
        numero2: int = random.randint(0, 9)
        expressao = f"{numero1} {operador_aleatorio} {numero2}"
        resultado: float = eval(expressao)
        return expressao, resultado

    elif dificuldade == 2:
        numero1: int = random.randint(10, 99)
        numero2: int = random.randint(10, 99)
        expressao = f"{numero1} {operador_aleatorio} {numero2}"
        resultado: float = eval(expressao)
        return expressao, resultado

    elif dificuldade == 3:
        numero1: int = random.randint(100, 999)
        numero2: int = random.randint(100, 999)
        expressao = f"{numero1} {operador_aleatorio} {numero2}"
        resultado: float = eval(expressao)
        return expressao, resultado

    elif dificuldade == 4:
        numero1: int = random.randint(1000, 9999)
        numero2: int = random.randint(1000, 9999)
        expressao = f"{numero1} {operador_aleatorio} {numero2}"
        resultado: float = eval(expressao)
        return expressao, resultado


def jogar() -> Tuple:
    nivel = int(input('Informe o nível de dificuldade desejado [1, 2, 3, 4]: '))
    resultado_retornado: Tuple = nivel_dificuldade(nivel)
    mostra_operacao: str = resultado_retornado[0]
    resultado_operacao: int = resultado_retornado[1]
    print(f'{mostra_operacao} = ?')
    resposta = int(input('Informe o valor da operação: '))
    print(resultado_operacao)
    return resposta, resultado_operacao, nivel


cont: int = 0
result: Tuple = jogar()
resposta_jogo: int = result[0]
resposta_jogador: int = result[1]
dif: int = result[2]

if resposta_jogador == resposta_jogo:
    cont += 1
    print('Resposta Correta! :)')
else:
    print('Resposta Errada! :/')

continuar: int = 1
while continuar == 1:
    jogar()
    if resposta_jogador == resposta_jogo:
        cont += 1
        print('Resposta Correta! :)')
    else:
        print('Resposta Errada! :/')
    continuar = int(input('Quer continuar jogando [1 = sim, 0 = não]? '))

print(f'Quantidade de pontos totais: {cont}')
