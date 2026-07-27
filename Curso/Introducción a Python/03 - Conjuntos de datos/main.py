precios = [100.5, 101.2, 99.8, 102.4]
activo = ("AAPL", "Acción", "NASDAQ")
portafolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 2,
}
mercados = {"NYSE", "NASDAQ", "SSE", "NASDAQ"}

print("Precios:", precios)
print("Primer precio:", precios[0])
print("Último precio:", precios[-1])

print("Activo:", activo)
print("Ticker:", activo[0])

print("Portafolio:", portafolio)
print("Acciones de AAPL:", portafolio["AAPL"])

portafolio["AAPL"] = 12
portafolio["GOOG"] = 1

print("Portafolio actualizado:", portafolio)
print("Mercados únicos:", mercados)
