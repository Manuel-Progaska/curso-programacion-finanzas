# Funciones

Las funciones permiten organizar código en bloques reutilizables.

En programación financiera son útiles para encapsular cálculos como rentabilidad, interés compuesto o valorización de instrumentos.

## Objetivos

- Definir funciones con `def`.
- Usar parámetros para entregar datos a una función.
- Usar `return` para devolver resultados.
- Evitar repetir código en cálculos financieros.

## Conceptos clave

Una función es un bloque de código con nombre. Se define una vez y puede usarse muchas veces.

Los parámetros son variables que la función recibe para trabajar. Por ejemplo, una función de rentabilidad necesita un precio inicial y un precio final.

`return` indica el resultado que la función entrega. Esto permite guardar el resultado en una variable, imprimirlo o usarlo en otro cálculo.

Usar funciones ayuda a escribir programas más claros. Si una fórmula financiera se repite muchas veces, conviene convertirla en función.

## Código

```python
def calcular_rentabilidad(precio_inicial, precio_final):
    rentabilidad = (precio_final - precio_inicial) / precio_inicial
    return rentabilidad


def calcular_capital_final(capital_inicial, tasa, periodos):
    capital = capital_inicial * (1 + tasa) ** periodos
    return capital


precio_inicial = 100
precio_final = 115

rentabilidad = calcular_rentabilidad(precio_inicial, precio_final)
print("Rentabilidad:", rentabilidad)

capital_final = calcular_capital_final(1000, 0.05, 5)
print("Capital final:", round(capital_final, 2))
```

## Explicación del código

`calcular_rentabilidad()` recibe dos precios. La fórmula `(precio_final - precio_inicial) / precio_inicial` calcula la variación porcentual entre ambos.

`calcular_capital_final()` aplica interés compuesto. La expresión `(1 + tasa) ** periodos` eleva el factor de crecimiento al número de periodos.

Después de definir las funciones, las llamamos con valores concretos. El resultado de cada llamada se guarda en una variable y luego se imprime.

Separar el cálculo en funciones hace que el código sea más fácil de probar. Si mañana queremos calcular rentabilidad para otro activo, no necesitamos escribir la fórmula otra vez.

## Errores comunes

- Olvidar los paréntesis al llamar una función.
- Confundir `print()` con `return`. `print()` muestra, `return` devuelve.
- Definir una función pero nunca llamarla.
- Entregar los parámetros en un orden incorrecto.

## Ejercicios

1. Crea una función que calcule la ganancia absoluta: `precio_final - precio_inicial`.
2. Crea una función que calcule el valor de una posición: `precio * cantidad`.
3. Llama `calcular_capital_final()` con distintos periodos.
4. Modifica la función de rentabilidad para imprimir el resultado como porcentaje.
