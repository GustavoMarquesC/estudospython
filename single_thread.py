import time

from threading import Thread

CONTADOR = 50000000


def contagem_regrassiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regrassiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
