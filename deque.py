"""
Podemos dizer que o deque é uma lista de alta desempenho.

"""

from collections import deque

deq = deque('Geek')

print(deq)

deq.append('y')

print(deq)

deq.appendleft('k')

print(deq)

#  Remover elementos

print(deq.pop())

print(deq)

print(deq.popleft())

print(deq)
