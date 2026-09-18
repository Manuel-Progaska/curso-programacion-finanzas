# Conjuntos de datos

Los conjuntos de datos permiten guardar varios valores en una misma variable. En Python podemos usar listas, tuplas, diccionarios y conjuntos para organizar precios, activos y portafolios.

## Objetivos

- Reconocer las principales colecciones de Python.
- Acceder, agregar, modificar y eliminar elementos.
- Elegir la colección adecuada según el problema.
- Aplicar colecciones a ejemplos financieros simples.

## Conceptos clave

| Tipo | Característica | ¿Se puede modificar? | Ejemplo |
|------|----------------|-----------------------|---------|
| `list` | Elementos ordenados | Sí | `[100.5, 101.2]` |
| `tuple` | Elementos ordenados | No | `("AAPL", "NASDAQ")` |
| `dict` | Pares clave-valor | Sí | `{"AAPL": 10}` |
| `set` | Elementos únicos | Sí | `{"NYSE", "NASDAQ"}` |

## 1. List: listas

Una `list` guarda elementos en orden. Puede contener distintos tipos de datos y puede modificarse después de ser creada.

### 1.1 Definir y consultar una lista

```python
precios = [100.5, 101.2, 99.8, 102.4]

print(precios)
print(precios[0])   # Primer elemento
print(precios[-1])  # Último elemento
print(len(precios))
```

Python comienza a contar las posiciones desde `0`. Intentar acceder a una posición inexistente produce un `IndexError`.

### 1.2 Modificar una lista

```python
precios = [100.5, 101.2, 99.8]

precios.append(102.4)
precios[0] = 100.8
precios.remove(99.8)

print(precios)
```

`append()` agrega un elemento al final, `remove()` elimina la primera coincidencia y `pop()` elimina un elemento según su posición.

### 1.3 Operaciones útiles

```python
precios = [100.5, 101.2, 99.8, 102.4]

print("Mínimo:", min(precios))
print("Máximo:", max(precios))
print("Suma:", sum(precios))
print("Promedio:", sum(precios) / len(precios))
```

## 2. Tuple: tuplas

Una `tuple` también guarda elementos en orden, pero no puede modificarse después de su creación. Es útil para datos que deberían permanecer fijos.

```python
activo = ("AAPL", "Acción", "NASDAQ")

print("Ticker:", activo[0])
print("Tipo:", activo[1])
print("Mercado:", activo[2])
```

Los valores se pueden desempaquetar en variables:

```python
ticker, tipo, mercado = activo
print(ticker, tipo, mercado)
```

La instrucción `activo[0] = "MSFT"` produciría un `TypeError`, porque las tuplas son inmutables.

## 3. Dict: diccionarios

Un `dict` relaciona claves con valores. Las claves no se repiten y permiten buscar información sin conocer su posición.

### 3.1 Definir y consultar un diccionario

```python
portafolio = {
    "AAPL": 10,
    "MSFT": 5,
    "TSLA": 2,
}

print(portafolio["AAPL"])
print(portafolio.get("GOOG", 0))
```

Los corchetes producen un `KeyError` si la clave no existe. El método `get()` permite indicar un valor alternativo.

### 3.2 Agregar, modificar y eliminar

```python
portafolio["AAPL"] = 12
portafolio["GOOG"] = 1
del portafolio["TSLA"]

print(portafolio)
```

También podemos consultar sus componentes:

```python
print(portafolio.keys())
print(portafolio.values())
print(portafolio.items())
```

## 4. Set: conjuntos

Un `set` guarda elementos únicos y no garantiza un orden. Es útil para eliminar duplicados o comprobar pertenencia.

```python
mercados = {"NYSE", "NASDAQ", "SSE", "NASDAQ"}

mercados.add("LSE")
mercados.discard("SSE")

print(mercados)
print("NASDAQ" in mercados)
```

Aunque `"NASDAQ"` aparece dos veces al crear el conjunto, se almacena una sola vez. `discard()` no produce error si el elemento no existe.

### 4.1 Operaciones entre conjuntos

```python
mercados_portafolio = {"NYSE", "NASDAQ"}
mercados_disponibles = {"NASDAQ", "LSE", "SSE"}

print(mercados_portafolio & mercados_disponibles)  # Intersección
print(mercados_portafolio | mercados_disponibles)  # Unión
print(mercados_portafolio - mercados_disponibles)  # Diferencia
```

## 5. Elegir una colección

- Usa una lista cuando importe el orden y los valores puedan cambiar.
- Usa una tupla cuando importe el orden y los valores deban permanecer fijos.
- Usa un diccionario cuando necesites relacionar una clave con un valor.
- Usa un conjunto cuando necesites valores únicos y el orden no sea importante.
