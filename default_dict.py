"""
dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) #  ?? KeyError

#  Exemplo

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  #  KeyError no dicionário comum, mas aqui não.

print(dicionario)
# Res: defaultdict(<function <lambda> at 0x000001CAD7D904A0>, {'curso': 'Programação em Python: Essencial', 'outro': 0})

"""
