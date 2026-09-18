precios = [100, 102, 101, 105, 107]

for precio in precios:
    print("Precio observado:", precio)

total = 0

for precio in precios:
    total = total + precio

print("Precio promedio:", total / len(precios))

capital = 1000
tasa = 0.05
periodos = 5

for periodo in range(1, periodos + 1):
    capital = capital * (1 + tasa)
    print("Periodo:", periodo, "Capital:", round(capital, 2))

objetivo = 1500
capital = 1000
periodo = 0

while capital < objetivo:
    capital = capital * (1 + tasa)
    periodo = periodo + 1

print("Periodos necesarios para alcanzar el objetivo:", periodo)

precios_con_error = [100, 102, -1, 105]

for precio in precios_con_error:
    if precio < 0:
        print("Precio inválido. Se detiene la lectura.")
        break
    print("Precio válido:", precio)

rentabilidades = [0.03, None, -0.01, 0.02]

for rentabilidad in rentabilidades:
    if rentabilidad is None:
        continue
    print("Rentabilidad:", rentabilidad)

portafolio = {"AAPL": 10, "MSFT": 5, "TSLA": 2}

for ticker, cantidad in portafolio.items():
    print("Activo:", ticker, "Cantidad:", cantidad)
