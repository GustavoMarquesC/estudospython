"""
Introdução ao módulo Unittest

Unittest -> Teste Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

#OBS: Teste Unitário não é específico da linguagem Python.

Para criar nosso testes, criamos classes que herdam de unittest.TestCase e a partir de então ganhamos todos os
'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Caso de teste para sua unidade

# Conhecendo as assertions

Métodos                                   Checa que
assertEqual(a, b)                         a == b
assertNotEqual(a, b)                      a != b
assertTrue(x)                             x é verdadeiro
assertFalse(x)                            x é falso
assertIs(a, b)                            a é b
assertIsNot(a, b)                         a não é b
assertIfNone(x)                           x é None
assertIfNotNone(x)                        x não é None
assertIn(a, b)                            a está em b
assertNotIn(a, b)                         a não está em b
assertIsInstance(a, b)                    a é instância de b
assertNotIsInstance(a, b)                 a não é instância de b

Por convenção, todos os testes em um test case, devem ter seu nome
"""

# Prática - Utilizando a abordagem TDD


