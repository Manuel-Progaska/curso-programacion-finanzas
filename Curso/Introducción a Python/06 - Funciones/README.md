# Funciones

Las funciones permiten organizar instrucciones en bloques reutilizables. En finanzas sirven para encapsular cálculos como rentabilidad, interés compuesto o valorización de posiciones.

## Objetivos

- Definir y llamar funciones.
- Entregar información mediante parámetros.
- Devolver resultados con `return`.
- Usar parámetros con valores predeterminados.
- Dividir un problema en cálculos reutilizables.

## Conceptos clave

| Elemento | Función |
|----------|---------|
| `def` | Inicia la definición de una función |
| Parámetro | Variable que la función espera recibir |
| Argumento | Valor entregado al llamar la función |
| `return` | Devuelve un resultado |

## 1. Definir y llamar una función

Una función se define con `def`, un nombre, paréntesis y dos puntos:

```python
def mostrar_bienvenida():
    print("Bienvenido al sistema financiero")


mostrar_bienvenida()
```

Definir la función no ejecuta su contenido. Para ejecutarla se debe llamar usando su nombre y paréntesis.

## 2. Parámetros y argumentos

Los parámetros permiten que una misma función trabaje con datos distintos:

```python
def calcular_valor_posicion(precio, cantidad):
    valor = precio * cantidad
    print("Valor de la posición:", valor)


calcular_valor_posicion(125.75, 10)
calcular_valor_posicion(80.50, 5)
```

`precio` y `cantidad` son parámetros. `125.75` y `10` son los argumentos de la primera llamada.

### 2.1 Argumentos por nombre

También se puede indicar a qué parámetro corresponde cada argumento:

```python
calcular_valor_posicion(cantidad=10, precio=125.75)
```

Esto mejora la claridad y permite cambiar el orden de los argumentos.

## 3. Return: devolver un resultado

`return` entrega un valor que puede guardarse o usarse en otro cálculo:

```python
def calcular_rentabilidad(precio_inicial, precio_final):
    rentabilidad = (precio_final - precio_inicial) / precio_inicial
    return rentabilidad


resultado = calcular_rentabilidad(100, 115)
print("Rentabilidad:", resultado)
```

No se debe confundir `print()` con `return`: `print()` muestra información y `return` la devuelve. Cuando se ejecuta `return`, la función termina.

## 4. Parámetros predeterminados

Un parámetro puede tener un valor que se usa cuando no se entrega otro:

```python
def calcular_comision(monto, tasa=0.01):
    return monto * tasa


print(calcular_comision(1000))
print(calcular_comision(1000, 0.005))
```

Los parámetros sin valor predeterminado deben escribirse antes que aquellos que sí lo tienen.

## 5. Documentar una función

Un `docstring` explica qué hace una función:

```python
def calcular_capital_final(capital_inicial, tasa, periodos):
    """Calcula el capital final usando interés compuesto."""
    return capital_inicial * (1 + tasa) ** periodos


capital_final = calcular_capital_final(1000, 0.05, 5)
print(round(capital_final, 2))
```

## 6. Alcance de las variables

Una variable creada dentro de una función es local y normalmente solo existe dentro de ella:

```python
def calcular_ganancia(precio_inicial, precio_final):
    ganancia = precio_final - precio_inicial
    return ganancia


resultado = calcular_ganancia(100, 115)
print(resultado)

# Esto produce un error fuera de la función:
# print(ganancia)
```

Conviene que las funciones reciban la información mediante parámetros y devuelvan resultados, en lugar de depender de variables externas.
