def mostrar_bienvenida():
    print("Bienvenido al sistema financiero")


def calcular_valor_posicion(precio, cantidad):
    return precio * cantidad


def calcular_rentabilidad(precio_inicial, precio_final):
    rentabilidad = (precio_final - precio_inicial) / precio_inicial
    return rentabilidad


def calcular_capital_final(capital_inicial, tasa, periodos):
    """Calcula el capital final usando interés compuesto."""
    capital = capital_inicial * (1 + tasa) ** periodos
    return capital


def calcular_comision(monto, tasa=0.01):
    return monto * tasa


mostrar_bienvenida()

valor_posicion = calcular_valor_posicion(precio=125.75, cantidad=10)
print("Valor de la posición:", valor_posicion)

precio_inicial = 100
precio_final = 115

rentabilidad = calcular_rentabilidad(precio_inicial, precio_final)
print("Rentabilidad:", rentabilidad)

capital_final = calcular_capital_final(1000, 0.05, 5)
print("Capital final:", round(capital_final, 2))

print("Comisión estándar:", calcular_comision(1000))
print("Comisión preferencial:", calcular_comision(1000, 0.005))
