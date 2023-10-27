"""
Por que testar nosso código?

Testes Automatizados!


          Aplicação Web
-------------------------------------------
|                                         |
|           Frontend e Backend            |
-------------------------------------------
|           Testes Automatizados          |
-------------------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código existe;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Teste garantem que a refatoração que costumamos fazer não tragam novos bugs;

TDD - Test Driven Development (Desenvolvimento Guiado por testes)
Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (Ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidades e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - red;
    - green;
    - refactor;
    
"""
class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando... ')


felix = Gato('Felix')
felix.miar()
print(felix.nome)
