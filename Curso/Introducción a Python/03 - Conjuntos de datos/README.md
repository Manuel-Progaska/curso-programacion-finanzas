# Conjuntos de datos

Los conjuntos de datos permiten guardar varios valores en una misma variable.

En Python usaremos listas, tuplas, diccionarios y conjuntos para organizar información financiera como precios, activos y portafolios.

## Objetivos

- Entender cuándo usar listas, tuplas, diccionarios y conjuntos.
- Acceder a elementos dentro de una colección.
- Actualizar información guardada en un diccionario.
- Reconocer estructuras útiles para datos financieros.

## Conceptos clave

Una lista guarda varios elementos en orden y puede modificarse. Es útil para precios históricos, retornos diarios o montos de transacciones.

Una tupla también guarda elementos en orden, pero normalmente se usa para datos que no deberían cambiar, como la descripción básica de un activo.

Un diccionario guarda pares `clave: valor`. Es muy útil cuando queremos asociar un identificador con un dato, por ejemplo ticker y cantidad de acciones.

Un conjunto guarda valores únicos. Si se repite un elemento, Python lo conserva solo una vez. Esto sirve para eliminar duplicados.

## Código

```python
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
```

## Explicación del código

`precios` es una lista con cuatro precios. Se accede al primer elemento con `precios[0]` porque Python cuenta desde cero. El último elemento se puede obtener con `precios[-1]`.

`activo` es una tupla que guarda información fija: ticker, tipo de instrumento y mercado. Para obtener el ticker usamos `activo[0]`.

`portafolio` es un diccionario. Sus claves son tickers y sus valores son cantidades. `portafolio["AAPL"]` devuelve la cantidad asociada a `AAPL`.

Luego actualizamos el diccionario: cambiamos la cantidad de `AAPL` y agregamos `GOOG`.

`mercados` es un conjunto. Aunque `NASDAQ` aparece dos veces al crearlo, el conjunto final lo guarda una sola vez.

## Errores comunes

- Intentar acceder a una posición que no existe en una lista.
- Olvidar que los índices comienzan en `0`.
- Buscar una clave que no existe en un diccionario.
- Esperar que un conjunto mantenga elementos repetidos.

## Ejercicios

1. Agrega un nuevo precio a la lista `precios`.
2. Crea un diccionario con precios por ticker.
3. Calcula manualmente el valor de una posición usando cantidad y precio.
4. Agrega un mercado repetido al conjunto y observa el resultado.
