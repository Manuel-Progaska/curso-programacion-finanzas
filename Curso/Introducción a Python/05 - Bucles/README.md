# Bucles

Los bucles permiten repetir instrucciones sin escribir el mismo código varias veces. Son útiles para recorrer precios, calcular acumulados y simular periodos de inversión.

## Objetivos

- Usar `for` para recorrer colecciones.
- Generar secuencias con `range()`.
- Usar `while` cuando no conocemos el número de repeticiones.
- Controlar un bucle con `break` y `continue`.
- Aplicar bucles a cálculos financieros simples.

## Conceptos clave

| Elemento | Uso |
|----------|-----|
| `for` | Recorre los elementos de una colección |
| `range()` | Genera una secuencia de enteros |
| `while` | Repite mientras una condición sea verdadera |
| `break` | Termina el bucle |
| `continue` | Pasa a la siguiente repetición |

## 1. For: recorrer una colección

Un bucle `for` toma cada elemento de una colección, uno a la vez:

```python
precios = [100, 102, 101, 105, 107]

for precio in precios:
    print("Precio observado:", precio)
```

La variable `precio` cambia de valor en cada repetición. Su nombre puede elegirse libremente, pero conviene usar uno que describa cada elemento.

### 1.1 Acumular valores

Una variable acumuladora guarda un resultado que se actualiza en cada repetición:

```python
precios = [100, 102, 101, 105, 107]
total = 0

for precio in precios:
    total = total + precio

promedio = total / len(precios)
print("Promedio:", promedio)
```

## 2. Range: repetir una cantidad definida

`range()` genera una secuencia de números enteros. El límite final no se incluye.

```python
for numero in range(5):
    print(numero)  # 0, 1, 2, 3, 4
```

Puede recibir un inicio, un límite y un paso:

```python
for periodo in range(1, 6):
    print(periodo)  # 1, 2, 3, 4, 5

for numero in range(0, 11, 2):
    print(numero)  # 0, 2, 4, 6, 8, 10
```

### 2.1 Proyectar capital

```python
capital = 1000
tasa = 0.05
periodos = 5

for periodo in range(1, periodos + 1):
    capital = capital * (1 + tasa)
    print("Periodo:", periodo, "Capital:", round(capital, 2))
```

Se usa `periodos + 1` porque el límite final de `range()` no se incluye.

## 3. While: repetir según una condición

Un bucle `while` se ejecuta mientras su condición sea verdadera:

```python
objetivo = 1500
capital = 1000
tasa = 0.05
periodo = 0

while capital < objetivo:
    capital = capital * (1 + tasa)
    periodo = periodo + 1

print("Periodos necesarios:", periodo)
```

Alguna variable de la condición debe cambiar dentro del bucle. De lo contrario, se puede crear un bucle infinito.

## 4. Break y continue

`break` termina el bucle inmediatamente:

```python
precios = [100, 102, -1, 105]

for precio in precios:
    if precio < 0:
        print("Precio inválido")
        break
    print(precio)
```

`continue` omite el resto de la repetición actual:

```python
rentabilidades = [0.03, None, -0.01, 0.02]

for rentabilidad in rentabilidades:
    if rentabilidad is None:
        continue
    print("Rentabilidad:", rentabilidad)
```

## 5. Recorrer un diccionario

El método `items()` permite obtener la clave y el valor:

```python
portafolio = {"AAPL": 10, "MSFT": 5, "TSLA": 2}

for ticker, cantidad in portafolio.items():
    print("Activo:", ticker, "Cantidad:", cantidad)
```
