def avalia_carro(km, litros):
    kml = km/litros
    if kml < 8:
        return 'Venda o carro!'
    if kml >= 8 or kml <= 14:
        return 'Econômico'
    if kml > 12:
        return 'Super Econômico'


print(avalia_carro(456, 10))
