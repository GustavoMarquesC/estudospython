import random

dados = []


def lanca_dado(qtd_lado):
    dado = random.randint(0, qtd_lado)
    return dado


quantidade_dado = int(input('Qual será a quantidade de dados lançados: '))
for num in range(quantidade_dado):
    quantidade_lados = int(input('Quantos lados terá o dado: '))
    dados.append(lanca_dado(quantidade_lados))

print(dados)
