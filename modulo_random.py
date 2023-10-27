"""
Módulo Random e o que são Módulo?

- Em Python, Módulo nada mais são que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função teste.

# Forma 1 - Importando todo o módulo (não recomendado)

import random

# random() -> gera um número pseudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o múdulo, todas as funções, atributos, classes e propriedades que estiverem dentro do
# módulo ficarão disponíveis (ficarão em Memória). Caso você saiba quais funções você precisa utilizar deste módulo,
# então esta não seria a forma ideal de utilização. Nós veremos umas forma melhora na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas umas
# função dentro do módulo random.

# Forma 2 -> Importanto uma função específica do módulo. (forma recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído.

# randint() -> gera valores pseudo-aleatórios entre ps valores estabelecidos.

from random import randint

# Gerador de apostas para a mega-sena

for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 60

from random import choice

# choice() -> Mostra um valor aleatório entre um itarável.

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""

from random import shuffle

# shuffle() -> tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())
