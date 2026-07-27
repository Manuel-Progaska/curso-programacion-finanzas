# Bucles

Los bucles permiten repetir instrucciones sin escribir el mismo código muchas veces.

Son útiles para recorrer precios, calcular acumulados o simular periodos de inversión.

## Objetivos

- Usar `for` para recorrer colecciones.
- Usar `range()` para repetir una tarea una cantidad definida de veces.
- Usar `while` para repetir mientras una condición sea verdadera.
- Simular crecimiento de capital en el tiempo.

## Conceptos clave

Un bucle `for` recorre una secuencia de valores. Es ideal cuando sabemos qué colección queremos procesar, por ejemplo una lista de precios.

`range()` genera una secuencia de números. Se usa mucho cuando necesitamos repetir algo por periodos, años o escenarios.

Un bucle `while` se ejecuta mientras una condición sea verdadera. Es útil cuando no sabemos de antemano cuántas repeticiones serán necesarias.

En finanzas, los bucles aparecen al calcular retornos históricos, proyectar capital en varios periodos, revisar transacciones o simular escenarios.

## Código

```python
precios = [100, 102, 101, 105, 107]

for precio in precios:
    print("Precio observado:", precio)

capital = 1000
tasa = 0.05
periodos = 5

for periodo in range(1, periodos + 1):
    capital = capital * (1 + tasa)
    print("Periodo:", periodo, "Capital:", round(capital, 2))

objetivo = 1500
capital = 1000
periodo = 0

while capital < objetivo:
    capital = capital * (1 + tasa)
    periodo = periodo + 1

print("Periodos necesarios para alcanzar el objetivo:", periodo)
```

## Explicación del código

El primer `for` recorre la lista `precios`. En cada repetición, la variable `precio` toma uno de los valores de la lista y se imprime.

Luego se define un capital, una tasa y una cantidad de periodos. El segundo `for` usa `range(1, periodos + 1)` para generar los números del 1 al 5. En cada periodo, el capital crece multiplicándose por `(1 + tasa)`.

La función `round(capital, 2)` redondea el resultado a dos decimales, lo que facilita la lectura de montos financieros.

Finalmente, el `while` calcula cuántos periodos se necesitan para que el capital alcance un objetivo. Como no sabemos el número exacto de periodos antes de empezar, `while` es una buena opción.

## Errores comunes

- Crear un `while` cuya condición nunca deja de cumplirse.
- Olvidar actualizar el contador dentro de un bucle.
- Confundir `range(1, 5)` con cinco repeticiones. Ese rango llega hasta 4.
- Modificar una lista mientras se recorre sin entender sus efectos.

## Ejercicios

1. Cambia la tasa a `0.03` y observa cuántos periodos se necesitan.
2. Cambia el objetivo a `2000`.
3. Agrega una lista de rentabilidades y recórrela con `for`.
4. Calcula la suma de todos los precios usando una variable acumuladora.
