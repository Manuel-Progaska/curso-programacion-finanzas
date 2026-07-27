rentabilidad = 0.08
riesgo = "medio"

if rentabilidad > 0.10:
    print("Rentabilidad alta")
elif rentabilidad > 0:
    print("Rentabilidad positiva")
else:
    print("Rentabilidad negativa")

if riesgo == "bajo":
    print("Perfil conservador")
elif riesgo == "medio":
    print("Perfil balanceado")
else:
    print("Perfil agresivo")

monto_inversion = 5000

if monto_inversion >= 1000 and rentabilidad > 0:
    print("La inversión cumple las condiciones mínimas")
else:
    print("La inversión no cumple las condiciones mínimas")
