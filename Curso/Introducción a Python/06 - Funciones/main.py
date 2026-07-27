def calcular_rentabilidad(precio_inicial, precio_final):
    rentabilidad = (precio_final - precio_inicial) / precio_inicial
    return rentabilidad


def calcular_capital_final(capital_inicial, tasa, periodos):
    capital = capital_inicial * (1 + tasa) ** periodos
    return capital


precio_inicial = 100
precio_final = 115

rentabilidad = calcular_rentabilidad(precio_inicial, precio_final)
print("Rentabilidad:", rentabilidad)

capital_final = calcular_capital_final(1000, 0.05, 5)
print("Capital final:", round(capital_final, 2))
