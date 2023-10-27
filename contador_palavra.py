contador = 0
contador2 = 0
contagem = []
indice = 0

with open("teste.txt", encoding='utf-8', mode="r") as file:
    allText = file.read()
    allText = allText.lower()
    words = list(map(str, allText.split()))
    for palavras in words:
        contador = contador + 1
    for palavras in words:
        if palavras == words[indice]:
            contador2 += 1
        else:
            contador2 = 1
    indice += indice


print(words)
print(contador)
for palavras in words:
    print(f"A palavra '{palavras}' ocorre {(words.count(palavras))} vezes.")
