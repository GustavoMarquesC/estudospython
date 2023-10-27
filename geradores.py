"""
Geradores

- Geradores (Generators) são iterators (iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.
Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criadas com Expressões Geradoras;

Diferança entra funções e Generator Functions (Funções Geradoras)

-----------------------------------------------------------------------------------
| Funções                                             | Generator Functions       |
-----------------------------------------------------------------------------------
| utilizam return                                     | utilizam yield            |
--------------------------------------------------------------------------------------------
| retorna uma vez                                     | pode utilizar yield múltiplas vezes|
-----------------------------------------------------------------------------------------------
| quando executada, retorna um valor                  | quando executada, retorna um generator|
-----------------------------------------------------------------------------------------------

gen = conta_at(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
"""

# Exemplo Generator Function


def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


print('\n')

gen = list(conta_at(10))
print(gen)
