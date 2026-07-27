# Clases

Las clases permiten crear nuestros propios tipos de objetos.

Un objeto puede agrupar datos y acciones. Por ejemplo, una inversión puede guardar capital, tasa y periodos, y además calcular su capital final.

## Objetivos

- Entender qué es una clase y qué es un objeto.
- Crear atributos para guardar estado.
- Crear métodos para definir comportamiento.
- Modelar una inversión simple usando programación orientada a objetos.

## Conceptos clave

Una clase es una plantilla para crear objetos. Define qué datos tendrá un objeto y qué acciones podrá realizar.

Un objeto es una instancia concreta de una clase. Si `Inversion` es la clase, `inversion = Inversion(...)` crea una inversión específica.

Los atributos son datos asociados al objeto. En este ejemplo, cada inversión tiene `nombre`, `capital_inicial` y `tasa_anual`.

Los métodos son funciones dentro de una clase. Representan acciones o cálculos que el objeto sabe hacer.

El método `__init__` se ejecuta cuando se crea el objeto. Se usa para inicializar sus atributos.

`self` representa al objeto actual. Permite acceder a sus atributos y métodos desde dentro de la clase.

## Código

```python
class Inversion:
    def __init__(self, nombre, capital_inicial, tasa_anual):
        self.nombre = nombre
        self.capital_inicial = capital_inicial
        self.tasa_anual = tasa_anual

    def capital_final(self, años):
        return self.capital_inicial * (1 + self.tasa_anual) ** años

    def resumen(self):
        print("Inversión:", self.nombre)
        print("Capital inicial:", self.capital_inicial)
        print("Tasa anual:", self.tasa_anual)


inversion = Inversion("Fondo balanceado", 1000, 0.06)

inversion.resumen()

resultado = inversion.capital_final(5)
print("Capital final a 5 años:", round(resultado, 2))
```

## Explicación del código

La clase `Inversion` define una estructura para representar una inversión. Al crear una inversión, entregamos nombre, capital inicial y tasa anual.

El método `capital_final()` recibe la cantidad de años y calcula el capital final usando interés compuesto.

El método `resumen()` imprime los datos principales de la inversión. No devuelve un valor, solo muestra información en pantalla.

Cuando ejecutamos `inversion = Inversion("Fondo balanceado", 1000, 0.06)`, Python crea un objeto con esos datos. Luego podemos pedirle al objeto que muestre su resumen o calcule su capital final.

## Errores comunes

- Olvidar `self` en los métodos de la clase.
- Confundir clase con objeto.
- Intentar usar un atributo que no fue definido en `__init__`.
- Llamar un método sin paréntesis.

## Ejercicios

1. Crea otra inversión con distinto capital y tasa.
2. Agrega un atributo `moneda`.
3. Agrega un método que calcule la ganancia final.
4. Modifica `resumen()` para mostrar la moneda de la inversión.
