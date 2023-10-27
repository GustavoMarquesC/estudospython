"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado de datetime

print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna a data de hora corrente
print(datetime.datetime.now())  # 2023-07-26 15:07:19.026530  BR 21/12/2018

# datetime.datetime(year, month, day, hour, minitu, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# alterar o horário para 16 horas, 0 minutos, 0 segungos, 0 microsegundo
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

import datetime


evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
"""

import datetime


evento = datetime.datetime.now()

# Acessa individual dos elementos de data e hora.

print(evento.year)  # ano
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

