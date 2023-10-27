"""
int, str, float, List, Set, Dict, etc

"""
"""
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols


# Literal type


# def pegar_statys(usuario: str) -> Literal['conectado', 'desconectado']:
#    pass


# def calcula_v1(operacao: str, num1: int, num2: int) -> None:
#    if operacao == '+':
#        print(f'{num1} + {num2} = {num1 + num2}')
#   elif operacao == '-':
#        print(f'{num1} - {num2} = {num1 - num2}')
#   else:
#       raise ValueError(f'Operação inválida {operacao!r}')


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
            print(f'{num1} + {num2} = {num1 + num2}')
       elif operacao == '-':
            print(f'{num1} - {num2} = {num1 - num2}')
       else:
           raise ValueError(f'Operação inválida {operacao!r}')



calcula_v2('+', 6, 4)
calcula_v2('-', 6, 4)
calcula_v2('*', 6, 4)

# Union


from typing import Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado

# Final


from typing import Final


NOME: Final = 'Geek'

print(NOME)

NOME = 'University'


print(NOME)
from typing import final
from typing import Final


# Final


@final
class Pessoa:
    pass


class Estudando():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudando):
    pass

    def estudar(self):
        print('Estudando e estagiando...')
        
    # Typed Dictionaries


from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3,=.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='vai', coisa=True)

print(outro)
"""

# Protocols

from typing import Protocol


class Curso(Protocol):
    titulo: str

    def __init__(self):
        Curso.titulo = 'Programação em Python'


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


v1 = Venda()
# c1 = Curso()
# c1.titulo = 'Programação em Python'

# estudar(v1)
estudar(v1)
