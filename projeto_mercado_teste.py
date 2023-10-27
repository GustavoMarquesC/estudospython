from typing import Dict, List

"""
Produto -> Tipo de produto
           Nome do produto
           Preço por unidade / KG
"""

caracteristicas_produtos: List = ['ip_produto', 'tipo_produto', 'nome_produto', 'preco_produto']
PRODUTO = {chave: None for chave in caracteristicas_produtos}
LISTA_PRODUTO: List = []
LISTA_CARRINHO: List = []
CARRINHO: List = []


def mostra_menu() -> None:
    print('-------------Menu Mercado-------------')
    print('Selecione uma opção:')
    print('-1- Cadastrar Produto')
    print('-2- Listar Produtos')
    print('-3- Comprar Produtos')
    print('-4- Mostrar carrinho')
    print('-5- Finalizar Compra')
    print('--------------------------------------')


def cadastrar_produto() -> Dict:
    PRODUTO['ip_produto']: int = 0
    PRODUTO['tipo_produto'] = str(input('Informe o tipo de produto: '))
    PRODUTO['nome_produto'] = str(input('Informe o nome do produto: '))
    PRODUTO['preco_produto'] = float(input('Informe o preço do produto: '))
    return PRODUTO


def carrinho(carrinho_produto, lista):
    for dicionario in lista:
        if carrinho_produto == dicionario['ip_produto']:
            CARRINHO.append(carrinho_produto)
    return CARRINHO


menu = 0
ip: int = 0


while menu != 5:
    mostra_menu()
    menu = int(input())
    if menu == 1:
        continuar_cadastrando: int = 1
        produto_cadastrado: Dict = cadastrar_produto()
        ip += 1
        produto_cadastrado['ip_produto'] = ip
        LISTA_PRODUTO.append(produto_cadastrado.copy())
        while continuar_cadastrando == 1:
            continuar_cadastrando = int(input('Deseja continuar cadastrando produtos [1 - sim, 0 - não]? '))
            if continuar_cadastrando == 1:
                produto_cadastrado = cadastrar_produto()
                ip += 1
                produto_cadastrado['ip_produto'] = ip
                LISTA_PRODUTO.append(produto_cadastrado.copy())
            else:
                break
    if menu == 2:
        for produto in LISTA_PRODUTO:
            print(produto)
    if menu == 3:
        if not LISTA_PRODUTO:
            print('Não há produto cadastrado no mercado!')
        else:
            ip_carrinho = int(input('Informe o produto que deseja comprar: '))
            LISTA_CARRINHO = (carrinho(ip_carrinho, LISTA_PRODUTO))
    if menu == 4:
        if not LISTA_PRODUTO:
            print('Não há produto cadastrado no mercado!')
        print('ITENS DENTRO DO CARRINHO')
        print(LISTA_CARRINHO)
