precios = [100.5, 101.2, 99.8, 102.4]

print("Precios:", precios)
print("Primer precio:", precios[0])
print("Último precio:", precios[-1])
print("Cantidad de precios:", len(precios))
print("Precio mínimo:", min(precios))
print("Precio máximo:", max(precios))
print("Precio promedio:", sum(precios) / len(precios))

precios.append(103.1)
precios[0] = 100.8
print("Precios actualizados:", precios)

activo = ("AAPL", "Acción", "NASDAQ")
ticker, tipo_activo, mercado = activo

print("Activo:", activo)
print("Ticker:", ticker)
print("Tipo:", tipo_activo)
print("Mercado:", mercado)

portafolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 2,
}

print("Portafolio:", portafolio)
print("Acciones de AAPL:", portafolio["AAPL"])
print("Acciones de GOOG:", portafolio.get("GOOG", 0))

portafolio["AAPL"] = 12
portafolio["GOOG"] = 1
del portafolio["TSLA"]

print("Portafolio actualizado:", portafolio)
print("Activos y cantidades:", portafolio.items())

mercados_portafolio = {"NYSE", "NASDAQ", "SSE", "NASDAQ"}
mercados_disponibles = {"NASDAQ", "LSE", "SSE"}

mercados_portafolio.add("LSE")
mercados_portafolio.discard("SSE")

print("Mercados únicos:", mercados_portafolio)
print("Mercados compartidos:", mercados_portafolio & mercados_disponibles)
print("Todos los mercados:", mercados_portafolio | mercados_disponibles)
