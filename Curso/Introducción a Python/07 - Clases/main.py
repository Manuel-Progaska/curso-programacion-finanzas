class Inversion:
    def __init__(self, nombre, capital_inicial, tasa_anual):
        self.nombre = nombre
        self.capital_inicial = capital_inicial
        self.tasa_anual = tasa_anual

    def capital_final(self, años):
        return self.capital_inicial * (1 + self.tasa_anual) ** años

    def resumen(self):
        print("Inversión:", self.nombre)
        print("Capital inicial:", self.capital_inicial)
        print("Tasa anual:", self.tasa_anual)


inversion = Inversion("Fondo balanceado", 1000, 0.06)

inversion.resumen()

resultado = inversion.capital_final(5)
print("Capital final a 5 años:", round(resultado, 2))

inversion_conservadora = Inversion("Fondo conservador", 1000, 0.03)
inversion_agresiva = Inversion("Fondo agresivo", 2000, 0.09)

print(
    "Capital final conservador:",
    round(inversion_conservadora.capital_final(5), 2),
)
print(
    "Capital final agresivo:",
    round(inversion_agresiva.capital_final(5), 2),
)


class CuentaInversion:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto


cuenta = CuentaInversion("Michael Scott", 1000)
cuenta.depositar(500)

print("Titular:", cuenta.titular)
print("Saldo después del depósito:", cuenta.saldo)
