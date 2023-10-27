import random

with open("teste.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

    print(random.choice(words))
