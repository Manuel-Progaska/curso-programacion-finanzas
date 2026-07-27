precios = [100, 102, 101, 105, 107]

for precio in precios:
    print("Precio observado:", precio)

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
