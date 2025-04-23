# operadores.py
# Este script demuestra cómo usar operadores aritméticos, lógicos y de comparación en Python.

# Operadores aritméticos
a = 10
b = 3
print("Operadores aritméticos:")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"Módulo: {a} % {b} = {a % b}")
print(f"Potencia: {a} ** {b} = {a ** b}")

# Operadores de comparación
print("\nOperadores de comparación:")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")

# Operadores lógicos
x = True
y = False
print("\nOperadores lógicos:")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Ejemplo combinado
print("\nEjemplo combinado:")
resultado = (a > b) and (a % b == 1)
print(f"¿{a} es mayor que {b} y su módulo es 1?: {resultado}")
