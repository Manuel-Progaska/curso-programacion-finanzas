# Condicionales

Los condicionales permiten que un programa tome decisiones.

Con `if`, `elif` y `else` podemos ejecutar distintos bloques de código según una condición.

## Objetivos

- Construir reglas de decisión con `if`, `elif` y `else`.
- Usar operadores de comparación.
- Combinar condiciones con operadores lógicos.
- Aplicar reglas simples a casos financieros.

## Conceptos clave

Una condición es una expresión que se evalúa como verdadera o falsa. Por ejemplo, `rentabilidad > 0` pregunta si la rentabilidad es positiva.

Python ejecuta el bloque indentado debajo de la primera condición verdadera. La indentación no es decoración: define qué instrucciones pertenecen a cada bloque.

Los operadores de comparación más comunes son:

- `>` mayor que.
- `<` menor que.
- `>=` mayor o igual que.
- `<=` menor o igual que.
- `==` igual a.
- `!=` distinto de.

Los operadores lógicos permiten combinar condiciones:

- `and`: ambas condiciones deben ser verdaderas.
- `or`: al menos una condición debe ser verdadera.
- `not`: invierte una condición.

## Código

```python
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
```

## Explicación del código

Primero se evalúa la rentabilidad. Si es mayor a `0.10`, se considera alta. Si no cumple esa condición, Python revisa si es mayor que `0`. Si tampoco cumple, cae en el bloque `else`.

Luego se clasifica el riesgo según el texto guardado en la variable `riesgo`. El operador `==` compara igualdad. En este caso, `"medio"` produce el mensaje `"Perfil balanceado"`.

Finalmente se evalúan dos condiciones al mismo tiempo: que el monto sea al menos `1000` y que la rentabilidad sea positiva. Como se usa `and`, ambas deben cumplirse para imprimir que la inversión cumple las condiciones mínimas.

## Errores comunes

- Usar `=` cuando se quiere comparar. Para comparar se usa `==`.
- Olvidar los dos puntos `:` después de `if`, `elif` o `else`.
- Escribir mal la indentación del bloque.
- Comparar texto con mayúsculas o espacios distintos.

## Ejercicios

1. Cambia la rentabilidad a `-0.03` y observa el resultado.
2. Cambia el riesgo a `"alto"`.
3. Agrega una condición para rechazar inversiones con monto menor a `500`.
4. Crea una regla que clasifique una inversión como atractiva si tiene rentabilidad mayor a `0.07` o riesgo bajo.
