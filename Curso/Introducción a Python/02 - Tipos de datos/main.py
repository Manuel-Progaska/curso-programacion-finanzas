nombre_activo = "AAPL"
mercado = "NASDAQ"
moneda = "USD"

cantidad_acciones = 10
periodos = 12

precio_accion = 125.75
tasa_mensual = 0.01

mercado_abierto = True
tiene_riesgo_alto = False

valor_posicion = precio_accion * cantidad_acciones
capital_proyectado = valor_posicion * (1 + tasa_mensual) ** periodos

print("Activo:", nombre_activo)
print("Mercado:", mercado)
print("Moneda:", moneda)
print("Cantidad de acciones:", cantidad_acciones)
print("Precio por acción:", precio_accion)
print("Valor de la posición:", valor_posicion)
print("Capital proyectado:", round(capital_proyectado, 2))
print("Mercado abierto:", mercado_abierto)
print("Riesgo alto:", tiene_riesgo_alto)

print("Tipo de nombre_activo:", type(nombre_activo))
print("Tipo de cantidad_acciones:", type(cantidad_acciones))
print("Tipo de precio_accion:", type(precio_accion))
print("Tipo de mercado_abierto:", type(mercado_abierto))

precio_texto = "150.25"
cantidad_texto = "20"

precio_convertido = float(precio_texto)
cantidad_convertida = int(cantidad_texto)

nuevo_valor_posicion = precio_convertido * cantidad_convertida

print("Precio como texto:", precio_texto)
print("Precio convertido a número:", precio_convertido)
print("Cantidad como texto:", cantidad_texto)
print("Cantidad convertida a entero:", cantidad_convertida)
print("Nuevo valor de la posición:", nuevo_valor_posicion)

rentabilidad = 0.075
rentabilidad_porcentaje = rentabilidad * 100
mensaje = "La rentabilidad fue de " + str(rentabilidad_porcentaje) + "%"

print(mensaje)

ticker = "AAPL"
mercado = "NASDAQ"

descripcion = ticker + " cotiza en " + mercado
print(descripcion)

separador = "-" * 30
print(separador)

precio_texto = "150.25"

# Esto produce error:
# resultado = precio_texto + 10

precio_texto = "150.25"
cantidad = 20

resultado = precio_texto * cantidad
print(resultado)

precio_texto = "150.25"
cantidad = 20

precio = float(precio_texto)
valor_posicion = precio * cantidad

print(valor_posicion)
