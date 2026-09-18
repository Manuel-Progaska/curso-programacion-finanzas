# Condicionales

Los condicionales permiten que un programa tome decisiones. Con `if`, `elif` y `else` podemos ejecutar distintos bloques de código según una condición.

## Objetivos

- Construir reglas de decisión con `if`, `elif` y `else`.
- Usar operadores de comparación y operadores lógicos.
- Entender la importancia de la indentación.
- Aplicar reglas de decisión a ejemplos financieros.

## Conceptos clave

| Palabra | Función |
|---------|---------|
| `if` | Evalúa la primera condición |
| `elif` | Evalúa otra condición si las anteriores fueron falsas |
| `else` | Se ejecuta si ninguna condición anterior fue verdadera |

Una condición produce un valor `True` o `False`. Python ejecuta solamente el primer bloque cuya condición sea verdadera.

## 1. If: primera condición

La sentencia `if` ejecuta un bloque cuando su condición es verdadera:

```python
rentabilidad = 0.08

if rentabilidad > 0:
    print("La inversión obtuvo una ganancia")
```

Los dos puntos (`:`) y la indentación son obligatorios. Las instrucciones indentadas pertenecen al condicional.

## 2. Else: alternativa

`else` permite definir qué hacer cuando la condición del `if` es falsa:

```python
saldo = 800
monto_inversion = 1000

if saldo >= monto_inversion:
    print("La compra puede realizarse")
else:
    print("Saldo insuficiente")
```

`else` no lleva condición, porque representa todos los casos restantes.

## 3. Elif: múltiples alternativas

`elif` permite evaluar varias condiciones en orden:

```python
rentabilidad = 0.08

if rentabilidad > 0.10:
    print("Rentabilidad alta")
elif rentabilidad > 0:
    print("Rentabilidad positiva")
elif rentabilidad == 0:
    print("Sin variación")
else:
    print("Rentabilidad negativa")
```

En este ejemplo se imprime `"Rentabilidad positiva"`. Aunque una condición posterior también pudiera cumplirse, Python deja de evaluar cuando encuentra la primera verdadera.

## 4. Operadores de comparación

| Operador | Significado |
|----------|-------------|
| `==` | Igual a |
| `!=` | Distinto de |
| `<` | Menor que |
| `>` | Mayor que |
| `<=` | Menor o igual que |
| `>=` | Mayor o igual que |

```python
precio = 125.75
precio_objetivo = 130

print(precio < precio_objetivo)
print(precio == precio_objetivo)
```

No se debe confundir `==`, que compara valores, con `=`, que asigna un valor a una variable.

## 5. Operadores lógicos

Los operadores lógicos combinan o invierten condiciones:

```python
monto_inversion = 5000
rentabilidad = 0.08
activo_bloqueado = False

cumple_minimos = monto_inversion >= 1000 and rentabilidad > 0
requiere_revision = rentabilidad > 0.15 or activo_bloqueado
puede_operar = not activo_bloqueado

print(cumple_minimos)
print(requiere_revision)
print(puede_operar)
```

- `and` exige que ambas condiciones sean verdaderas.
- `or` exige que al menos una condición sea verdadera.
- `not` invierte el resultado de una condición.

## 6. Condicionales anidados

Un condicional puede contener otro condicional:

```python
mercado_abierto = True
saldo_suficiente = True

if mercado_abierto:
    if saldo_suficiente:
        print("Orden enviada")
    else:
        print("Saldo insuficiente")
else:
    print("Mercado cerrado")
```

Cuando sea posible, los operadores lógicos ayudan a evitar demasiados niveles de anidación.
