# Tipos de datos

Los tipos de datos permiten representar distintos valores en un programa: texto, números enteros, números decimales y valores lógicos.

## Objetivos

- Reconocer los tipos de datos básicos en Python.
- Usar texto, números enteros, números decimales y booleanos.
- Entender la diferencia entre un número y un texto que parece número.
- Convertir datos cuando sea necesario.
- Aplicar tipos de datos a ejemplos financieros simples.

## Conceptos clave

Python usa distintos tipos según el valor almacenado:

| Tipo | Nombre común | Descripción | Ejemplo |
|------|--------------|-------------|---------|
| `str` | String o texto | Cadenas de caracteres | `"AAPL"` |
| `int` | Entero | Números sin decimales | `10` |
| `float` | Decimal | Números con decimales | `125.75` |
| `bool` | Booleano | Valor lógico verdadero o falso | `True` |


## 1. String: texto

Un `string` es una cadena de caracteres, los cuales pueden ser letras, números y cualquier caracter especial (ejemplo: %&@). Mientras los caracteres esten definidos de la forma correcta, python siempre lo va a interpretar como texto.

### 1.1 Definir un string

Hay 4 formas de definir un string:

```python
# Comillas simples
nombre_cliente = 'Michael'

# Comillas dobles
apellido_cliente = "Scott"

# Triple comilla simple
detalle_cliente = '''
Gerente Regional de Dunfler Muffin Pensilvanea.
'''

# Triple comilla doble
perfil_inversionista = """
Hombre de 40 año, clase media alta con patrimonio valorado
en USD 60,000. Sin experiencia en inversiones y cuyo objetivo
es complementar su jubilación.
"""

```

Aunque un texto contenga números, sigue siendo texto:

```python
precio_texto = "150.25"
```

Ese valor se ve como número, pero Python no lo tratará como número.

### 1.2 Funciones
```python
# Mayúsculas y minúsculas
ticker = "Aapl"
print("Función upper: ", ticker, ticker.upper())
print("Función lower: ", ticker, ticker.lower())

# Buscar y reemplazar
mensaje = "Precio de Apple"
print("Función replace: ", mensaje, mensaje.replace("Apple", "AAPL"))

# Dividir por un caracter en específico
datos = "AAPL,USD,125.75"
print("Función split: ", mensaje, datos.split(","))

# Eliminar caracteres vacíos
texto_sucio = "  AAPL  "
print("Función strip: ", texto_sucio, texto_sucio.strip())

# Formatear texto
perfil = "Agresivo"
mensaje = f"El apetito por riesgo del cliente es: {perfil}"
print("Formateo: ", mensaje)
```

### 1.3 Operaciones matemáticas con texto
En Python, los textos no se comportan como números. Sin embargo, al aplicar operadores matemáticos a strings, se pueden obtener resultados

#### Concatenar texto con `+`

Cuando usamos `+` entre strings, Python une los textos. A esto se le llama concatenación.

```python
ticker = "AAPL"
mercado = "NASDAQ"

descripcion = ticker + " cotiza en " + mercado
print(descripcion)
```

Resultado esperado:

```text
AAPL cotiza en NASDAQ
```

En este caso, `+` no suma valores, solo une texto.

#### Repetir texto con `*`

Python también permite multiplicar un string por un número entero. Esto repite el texto.

```python
separador = "-" * 30
print(separador)
```

Resultado esperado:

```text
------------------------------
```

Esto puede ser útil para ordenar salidas en consola, pero no corresponde a una multiplicación financiera.


## 2. Integer: números enteros

Un `integer` o `int` representa un número sin parte decimal. Puede ser positivo, negativo o cero.

```python
cantidad_acciones = 10
numero_transacciones = 25
dias_hasta_vencimiento = 30
saldo_puntos = -5
```

Los enteros se escriben sin comillas. Si se usan comillas, Python los interpreta como texto.

```python
cantidad = 10          # int
cantidad_texto = "10"  # str

print(type(cantidad))
print(type(cantidad_texto))
```

### 2.1 Operaciones con enteros

Con valores `int` se pueden realizar operaciones matemáticas:

```python
acciones_compradas = 10
acciones_vendidas = 3

acciones_disponibles = acciones_compradas - acciones_vendidas
acciones_totales = acciones_compradas + 5
acciones_repartidas = acciones_compradas // 3
acciones_restantes = acciones_compradas % 3

print("Acciones disponibles:", acciones_disponibles)
print("Acciones totales:", acciones_totales)
print("Acciones por grupo:", acciones_repartidas)
print("Acciones restantes:", acciones_restantes)
```

El operador `//` realiza una división entera y `%` obtiene el resto de una división. En cambio, `/` siempre entrega un resultado de tipo `float`, aunque la división sea exacta.

```python
print(10 / 2)   # 5.0
print(10 // 3)  # 3
print(10 % 3)   # 1
```

### 2.2 Convertir un valor a entero

La función `int()` convierte un valor compatible a número entero:

```python
cantidad_texto = "20"
cantidad = int(cantidad_texto)

print(cantidad)
print(type(cantidad))
```

Al convertir un `float`, Python elimina la parte decimal; no redondea el valor.

```python
precio = 125.75
precio_entero = int(precio)

print(precio_entero)  # 125
```

Un texto decimal como `"125.75"` no puede convertirse directamente con `int()`. Primero debe convertirse a `float`:

```python
precio_texto = "125.75"
precio_entero = int(float(precio_texto))
```

## 3. Float: números decimales

Un `float` representa números con parte decimal. En Python, el separador decimal es el punto (`.`), no la coma.

```python
precio_accion = 125.75
tasa_interes = 0.05
rentabilidad = -0.023
```

Los `float` son útiles para representar precios, tasas, rentabilidades y porcentajes.

### 3.1 Operaciones con decimales

Los valores `float` permiten realizar las operaciones matemáticas habituales:

```python
precio_accion = 125.75
cantidad_acciones = 10

valor_posicion = precio_accion * cantidad_acciones
comision = valor_posicion * 0.01
valor_final = valor_posicion - comision

print("Valor de la posición:", valor_posicion)
print("Comisión:", comision)
print("Valor después de comisión:", valor_final)
```

También se pueden combinar valores `int` y `float`. El resultado será normalmente un `float`.

```python
capital = 1000
tasa = 0.05
interes = capital * tasa

print(interes)        # 50.0
print(type(interes))  # <class 'float'>
```

### 3.2 Redondear decimales

La función `round()` permite redondear un número a una cantidad determinada de decimales:

```python
capital = 1000
tasa_mensual = 0.01
periodos = 12

capital_proyectado = capital * (1 + tasa_mensual) ** periodos

print(capital_proyectado)
print(round(capital_proyectado, 2))
```

Los números `float` pueden mostrar pequeñas diferencias de precisión debido a cómo se almacenan internamente. Para ejemplos introductorios se puede usar `round()`. En aplicaciones financieras reales que exigen cálculos monetarios exactos, se recomienda usar el tipo `Decimal`.

### 3.3 Convertir un valor a decimal

La función `float()` convierte un valor compatible a número decimal:

```python
precio_texto = "150.25"
precio = float(precio_texto)

print(precio)
print(type(precio))
```

La conversión fallará si el texto contiene caracteres que no forman un número válido:

```python
# Esto produce un error:
# precio = float("USD 150.25")
```

## 4. Bool: verdadero o falso

Un `boolean` o `bool` representa solamente dos valores posibles: `True` y `False`. Ambos se escriben con la primera letra en mayúscula y sin comillas.

```python
mercado_abierto = True
tiene_riesgo_alto = False
```

Los booleanos permiten representar estados y evaluar condiciones.

### 4.1 Comparaciones

Las comparaciones producen un resultado booleano:

```python
precio_actual = 125.75
precio_objetivo = 130.00
cantidad_acciones = 10

print(precio_actual < precio_objetivo)   # True
print(precio_actual == precio_objetivo)  # False
print(cantidad_acciones >= 10)           # True
print(cantidad_acciones != 0)            # True
```

Los operadores de comparación más comunes son:

| Operador | Significado |
|----------|-------------|
| `==` | Igual a |
| `!=` | Distinto de |
| `<` | Menor que |
| `>` | Mayor que |
| `<=` | Menor o igual que |
| `>=` | Mayor o igual que |

No se debe confundir `==`, que compara dos valores, con `=`, que asigna un valor a una variable.

### 4.2 Operadores lógicos

Los operadores `and`, `or` y `not` permiten combinar o invertir valores booleanos:

```python
mercado_abierto = True
saldo_suficiente = True
activo_bloqueado = False

puede_comprar = mercado_abierto and saldo_suficiente
requiere_revision = activo_bloqueado or not saldo_suficiente

print("Puede comprar:", puede_comprar)
print("Requiere revisión:", requiere_revision)
```

- `and` devuelve `True` cuando ambas condiciones son verdaderas.
- `or` devuelve `True` cuando al menos una condición es verdadera.
- `not` invierte el valor: `True` pasa a `False` y viceversa.

### 4.3 Convertir un valor a booleano

La función `bool()` convierte un valor a booleano. El número `0`, el texto vacío `""` y el valor `None` se convierten en `False`. La mayoría de los demás valores se convierten en `True`.

```python
print(bool(0))       # False
print(bool(10))      # True
print(bool(""))      # False
print(bool("AAPL"))  # True
```

Es importante recordar que cualquier texto no vacío es `True`, incluso el texto `"False"`:

```python
print(bool("False"))  # True
```
