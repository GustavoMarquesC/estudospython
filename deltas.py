"""
Trabalhando com Deltas de data e hora.

data_inicial = dd/mm/yyyy 12:55:34:812984
data_final = dd/mm/yyyy 13:34:23:094332

delta = data_inial - data_final

import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2024, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas... ')
"""

import datetime

data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento = data_compra + regra_boleto
print(vencimento)
