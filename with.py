"""
Bloco With

# 1 - Abrimos o arquivo
# 2 - Trabalhamos o arquivo
# 3 - Fechamos o arquivo

O block With é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco With

"""

# O bloco With - Forma Pythônica de manipular arquivos

with open('texto.txt', encoding='utf-8', mode="r") as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)
