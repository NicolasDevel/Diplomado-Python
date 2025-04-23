# parametros_y_retorno.py

"""
Este archivo contiene ejemplos de funciones con parámetros y valores de retorno.
Incluye ejemplos con anotaciones de tipos para mayor claridad y robustez.
"""

# Ejemplo 1: Función con parámetros y un retorno simple
def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros y devuelve el resultado."""
    return a * b

# Uso de la función
resultado = multiplicar(4, 5)
print(f"El producto de 4 y 5 es: {resultado}")

# Ejemplo 2: Parámetros con valores por defecto y anotaciones de tipos
def calcular_potencia(base: float, exponente: int = 2) -> float:
    """
    Calcula la potencia de un número.
    Parámetros:
        base (float): La base de la potencia.
        exponente (int): El exponente (por defecto, 2).
    Retorno:
        float: El resultado de la base elevada al exponente.
    """
    return base ** exponente

# Llamadas a la función con y sin el argumento opcional
resultado_por_defecto = calcular_potencia(3)
resultado_personalizado = calcular_potencia(2, 3)

print(f"3 elevado al cuadrado (por defecto) es: {resultado_por_defecto}")
print(f"2 elevado a la 3 es: {resultado_personalizado}")

# Ejemplo 3: Función con múltiples tipos de parámetros
def presentar_persona(nombre: str, edad: int, ciudad: str = "Bogotá") -> str:
    """
    Presenta información sobre una persona.
    Parámetros:
        nombre (str): El nombre de la persona.
        edad (int): La edad de la persona.
        ciudad (str): La ciudad de residencia (por defecto, Bogotá).
    Retorno:
        str: Una descripción de la persona.
    """
    return f"{nombre} tiene {edad} años y vive en {ciudad}."

# Llamadas a la función
descripcion_1 = presentar_persona("Nicolás", 29)
descripcion_2 = presentar_persona("Laura", 34, "Medellín")

print(descripcion_1)
print(descripcion_2)

# Ejemplo 4: Función que retorna múltiples valores
def operaciones_aritmeticas(a: float, b: float) -> tuple[float, float, float, float | None]:
    """
    Realiza varias operaciones aritméticas.
    Parámetros:
        a (float): El primer número.
        b (float): El segundo número.
    Retorno:
        tuple: Contiene la suma, resta, multiplicación y división de los números.
               Si la división no es posible (división por cero), devuelve None en su lugar.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return suma, resta, multiplicacion, division

# Uso de la función
resultado_operaciones = operaciones_aritmeticas(10, 2)
print(f"Resultados: Suma={resultado_operaciones[0]}, Resta={resultado_operaciones[1]}, Multiplicación={resultado_operaciones[2]}, División={resultado_operaciones[3]}")

# Fin del archivo
