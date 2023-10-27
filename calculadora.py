def calcular(tipo_operacao, primeiro_numero, segundo_numero):
    if simbolo == '+':
        return primeiro_numero + segundo_numero
    if tipo_operacao == '-':
        return primeiro_numero - segundo_numero
    if tipo_operacao == '/':
        return primeiro_numero / segundo_numero
    if tipo_operacao == '*':
        return primeiro_numero * segundo_numero


simbolo = str(input('Qual será o tipo de operação? '))
num1 = int(input('Informe o primeiro número da operação: '))
num2 = int(input('Informe o segundo número da operação: '))

print(calcular(simbolo, num1, num2))
