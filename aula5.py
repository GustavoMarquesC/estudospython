def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso


    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Geek University', idade=37, peso=69.5)
print(p.__dict__)
