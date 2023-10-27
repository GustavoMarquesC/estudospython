"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores separador por vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6

"geek", "university", "python", "ciência", "dados"

# Separador por ponto de vírgula
1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ciência"; "dados"

# Separador por espaço
1 2 3 4 5 6

"geek" "university" "python" "ciência" "dados"

http://dados.gov.br/dataset

# Reader


from csv import reader


with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')
"""

# DictReader

from csv import DictReader


with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um orderdict
        print(f"{linha['None']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
        


