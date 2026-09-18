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
activo_bloqueado = False

if monto_inversion >= 1000 and rentabilidad > 0:
    print("La inversión cumple las condiciones mínimas")
else:
    print("La inversión no cumple las condiciones mínimas")

if rentabilidad > 0.15 or activo_bloqueado:
    print("La inversión requiere revisión")

if not activo_bloqueado:
    print("El activo está disponible para operar")

mercado_abierto = True
saldo_suficiente = monto_inversion >= 1000

if mercado_abierto:
    if saldo_suficiente:
        print("Orden enviada")
    else:
        print("Saldo insuficiente")
else:
    print("Mercado cerrado")
