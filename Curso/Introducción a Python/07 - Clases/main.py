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
