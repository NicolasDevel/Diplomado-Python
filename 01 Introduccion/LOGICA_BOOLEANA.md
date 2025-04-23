# Lógica Booleana en Python

La lógica booleana es la base de la toma de decisiones en la programación. En Python, se representa a través del tipo de datos `bool`, que tiene solo dos valores posibles: **`True`** y **`False`**. Estos valores se generan al evaluar expresiones lógicas.

## Operadores Booleanos

### 1. Operadores de Comparación
Se utilizan para comparar valores y devuelven `True` o `False`.

| Operador | Descripción              | Ejemplo         | Resultado |
|----------|--------------------------|-----------------|-----------|
| `==`     | Igual a                  | `5 == 5`        | `True`    |
| `!=`     | Distinto de              | `5 != 3`        | `True`    |
| `>`      | Mayor que                | `7 > 3`         | `True`    |
| `<`      | Menor que                | `4 < 6`         | `True`    |
| `>=`     | Mayor o igual que        | `5 >= 5`        | `True`    |
| `<=`     | Menor o igual que        | `3 <= 4`        | `True`    |

### 2. Operadores Lógicos
Se utilizan para combinar expresiones booleanas.

| Operador | Descripción           | Ejemplo                 | Resultado |
|----------|-----------------------|-------------------------|-----------|
| `and`    | Devuelve `True` si **ambas** expresiones son `True` | `True and False` | `False` |
| `or`     | Devuelve `True` si **al menos una** expresión es `True` | `True or False`  | `True`  |
| `not`    | Invierte el valor booleano  | `not True`          | `False`  |

### 3. Operadores de Inclusión
Verifican si un elemento está en una colección.

| Operador  | Descripción          | Ejemplo               | Resultado |
|-----------|----------------------|-----------------------|-----------|
| `in`      | Devuelve `True` si un elemento está presente | `'a' in 'hola'`  | `True`    |
| `not in`  | Devuelve `True` si un elemento **no** está presente | `'z' not in 'hola'` | `True`    |

---

## Tabla de Verdad
### Operador `and`
| Expresión 1 | Expresión 2 | Resultado |
|-------------|-------------|-----------|
| `True`      | `True`      | `True`    |
| `True`      | `False`     | `False`   |
| `False`     | `True`      | `False`   |
| `False`     | `False`     | `False`   |

### Operador `or`
| Expresión 1 | Expresión 2 | Resultado |
|-------------|-------------|-----------|
| `True`      | `True`      | `True`    |
| `True`      | `False`     | `True`    |
| `False`     | `True`      | `True`    |
| `False`     | `False`     | `False`   |

### Operador `not`
| Expresión | Resultado |
|-----------|-----------|
| `True`    | `False`   |
| `False`   | `True`    |

---

## Ejemplos Prácticos
```python
# Comparaciones simples
a = 10
b = 5
print(a > b)  # True
print(a == b)  # False

# Uso de operadores lógicos
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Verificar pertenencia
texto = "Python"
print("y" in texto)    # True
print("z" not in texto)  # True


#Proposicional en Python
La **lógica proposicional** se utiliza para representar expresiones compuestas mediante conectores lógicos como **"y"** (and), **"o"** (or), y **"no"** (not). Estas expresiones están formadas por **proposiciones**, que son enunciados que pueden ser verdaderos o falsos.

En programación, la lógica proposicional se aplica utilizando los operadores lógicos de Python. Aquí te muestro ejemplos prácticos para entender cómo funcionan.

---

## Proposiciones Básicas
Una proposición es un enunciado simple que puede ser `True` o `False`.

- **p:** "Hoy es lunes"
- **q:** "Está lloviendo"

En Python, estas proposiciones pueden representarse como variables booleanas:
```python
p = True  # Hoy es lunes
q = False # No está lloviendo
