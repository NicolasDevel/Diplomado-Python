# introduccion_funciones.py

"""
Este archivo contiene ejemplos básicos de funciones en Python.
Aprenderás a definir, llamar y entender funciones simples.
"""

# Ejemplo 1: Definir una función simple
def saludar():
    """Imprime un mensaje de saludo en la consola."""
    print("¡Hola, Mundo!")

# Llamada a la función
saludar()

# Ejemplo 2: Función con parámetros
def saludar_con_nombre(nombre):
    """Imprime un saludo personalizado en la consola."""
    print(f"¡Hola, {nombre}!")

# Llamada a la función con un argumento
saludar_con_nombre("Nicolás")

# Ejemplo 3: Función con retorno de valor
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

# Uso de la función con retorno
resultado = sumar(5, 7)
print(f"La suma de 5 y 7 es: {resultado}")

# Ejemplo 4: Documentación y funciones
def describir_animal(animal="gato"):
    """
    Describe brevemente un animal.
    Parámetros:
        animal (str): El nombre del animal. Valor por defecto: "gato".
    Retorno:
        str: Una descripción del animal.
    """
    return f"El {animal} es un animal fascinante."

# Llamada a la función con y sin argumentos
descripcion_por_defecto = describir_animal()
descripcion_personalizada = describir_animal("perro")

print(descripcion_por_defecto)
print(descripcion_personalizada)

# Fin del archivo
