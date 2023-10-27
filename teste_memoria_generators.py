"""
Teste de memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 com lista 449MB
for n in fib_lista(100):
    print(n)

"""


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Função usando geradores


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a


# Teste 2 Geradores 3MB
for n in fib_lista(1000):
    print(n)
