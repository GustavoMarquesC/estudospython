"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa pare
de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:
try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema


try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.
# Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre tratar de forma específica

# Exemplo 3 - tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando um função inexistente')


try:
    len(5)
except TypeError:
    print('Você está utilizando um função inexistente')


# Exemplo 5 - Com detalhes do erro

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

    # Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    print('Geek'[9])
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as erro:
    print(f'Deu TypeError: {erro}')
except:
    print('Deu um erro diferente')

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}

print(pega_valor(dic, 8))
"""



