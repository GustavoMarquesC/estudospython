def verifica_palindromo(palavra_invertida):
    txt = palavra_invertida[::-1]
    if txt == palavra_invertida:
        return 'É um palíndromo'
    if txt != palavra_invertida:
        return 'Não é um palíndromo'


palavra = str(input('Informe um palavra: '))

print(verifica_palindromo(palavra))
