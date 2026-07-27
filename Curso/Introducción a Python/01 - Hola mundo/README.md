# Hola mundo

## Objetivos

- Ejecutar un programa simple en Python.
- Usar `print()` para mostrar texto, variables y resultados.
- Crear variables para guardar información.
- Realizar un cálculo financiero básico.

## Conceptos clave

-   Terminal.
-   script
-   función


## 1. Ejecutar script de python
El archivo que contiene código de python `scripts`. 

los scripts de python tienen la extensión `.py` (ejemplo: `main.py`).

Los scripts de python se ejecutan por medio de una `Terminal` que tiene instalado el `interprete de python`. A continuación se muestra cómo ejecutar un archivo desde distintas terminal

```bash
# Windows
python main.py

# Mac y Linux
python3 main.py
```

## 2. Print en Terminal
Un programa en Python es una secuencia de instrucciones. El interprete de python lee el archivo desde la primera línea hasta la última y ejecuta las instrucciones en ese orden.

La función `print()` permite mostrar

```python
print("Hola mundo")
print("Bienvenidos al curso Programación en Finanzas")
```

## 3. Variables
Una variable permite guardar un valor con un nombre. 

```python
nombre = "John"
apellido = "Smith"
print("Hola", nombre, apellido)
```

Las variables pueden redefinirse el mismo script, por lo que en un punto determinado del script, la variable puede tener un valor determinado, y luego puede ser redefinida a otro valor

```python
nombre = "Michael"
apellido = "Scott"
print("Hola", nombre, apellido)

nombre = "Jim"
apellido = "Hallper"
print("Hola", nombre, apellido)
```