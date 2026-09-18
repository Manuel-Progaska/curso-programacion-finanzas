# Clases

Las clases permiten crear tipos de objetos propios. Un objeto agrupa datos y acciones; por ejemplo, una inversión puede guardar su capital y tasa, además de calcular su capital final.

## Objetivos

- Entender la diferencia entre una clase y un objeto.
- Inicializar objetos con `__init__`.
- Guardar información en atributos.
- Definir comportamiento mediante métodos.
- Modelar una inversión simple.

## Conceptos clave

| Concepto | Descripción |
|----------|-------------|
| Clase | Plantilla que define datos y comportamientos |
| Objeto | Instancia concreta de una clase |
| Atributo | Dato asociado a un objeto |
| Método | Función definida dentro de una clase |
| `self` | Referencia al objeto actual |

## 1. Definir una clase

Una clase se define con la palabra `class`. Por convención, su nombre comienza con mayúscula:

```python
class Inversion:
    pass
```

`pass` indica que el bloque está vacío y evita un error de sintaxis. Una clase se convierte en objeto al llamarla:

```python
inversion = Inversion()

print(type(inversion))
```

`Inversion` es la clase e `inversion` es un objeto creado a partir de ella.

## 2. Init y atributos

El método `__init__` se ejecuta automáticamente al crear un objeto. Se utiliza para guardar su estado inicial:

```python
class Inversion:
    def __init__(self, nombre, capital_inicial, tasa_anual):
        self.nombre = nombre
        self.capital_inicial = capital_inicial
        self.tasa_anual = tasa_anual


inversion = Inversion("Fondo balanceado", 1000, 0.06)

print(inversion.nombre)
print(inversion.capital_inicial)
print(inversion.tasa_anual)
```

`self.nombre`, `self.capital_inicial` y `self.tasa_anual` son atributos. Cada objeto mantiene sus propios valores.

## 3. Métodos

Un método es una función dentro de una clase. Su primer parámetro es `self`:

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
```

Los métodos se llaman desde el objeto:

```python
inversion = Inversion("Fondo balanceado", 1000, 0.06)

inversion.resumen()
resultado = inversion.capital_final(5)

print("Capital final:", round(resultado, 2))
```

Python entrega automáticamente el objeto como `self`. Por eso solo se proporciona el argumento `5` al llamar `capital_final()`.

## 4. Crear varios objetos

Una clase puede utilizarse para crear objetos independientes:

```python
inversion_conservadora = Inversion("Fondo conservador", 1000, 0.03)
inversion_agresiva = Inversion("Fondo agresivo", 2000, 0.09)

print(inversion_conservadora.capital_final(5))
print(inversion_agresiva.capital_final(5))
```

Cambiar un atributo de un objeto no modifica los demás:

```python
inversion_conservadora.capital_inicial = 1500

print(inversion_conservadora.capital_inicial)
print(inversion_agresiva.capital_inicial)
```

## 5. Modificar el estado

Un método también puede modificar atributos:

```python
class CuentaInversion:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto


cuenta = CuentaInversion("Michael Scott", 1000)
cuenta.depositar(500)

print(cuenta.saldo)
```

El objeto conserva el nuevo saldo después de ejecutar `depositar()`.

## 6. Errores comunes

- Olvidar `self` como primer parámetro de un método.
- Confundir la clase con uno de sus objetos.
- Intentar usar un atributo que no fue inicializado.
- Llamar un método sin paréntesis.
- Escribir un nombre de clase en minúscula, en contra de la convención de Python.
