# lambdas.py

"""
Este archivo contiene ejemplos de funciones lambda en Python.
Las funciones lambda son funciones anónimas que se definen en una sola línea.
"""

# Ejemplo 1: Función lambda para sumar dos números
suma = lambda x, y: x + y

# Uso de la función lambda
resultado_suma = suma(5, 3)
print(f"La suma de 5 y 3 es: {resultado_suma}")

# Ejemplo 2: Lambda para calcular el cuadrado de un número
cuadrado = lambda x: x ** 2

resultado_cuadrado = cuadrado(4)
print(f"El cuadrado de 4 es: {resultado_cuadrado}")

# Ejemplo 3: Filtrar una lista con lambda y filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números pares en la lista: {numeros_pares}")

# Ejemplo 4: Mapear una lista con lambda y map
dobles = list(map(lambda x: x * 2, numeros))
print(f"Cada número en la lista multiplicado por 2: {dobles}")

# Ejemplo 5: Ordenar una lista de tuplas con lambda
personas = [("Ana", 25), ("Luis", 30), ("Pedro", 20)]
ordenadas_por_edad = sorted(personas, key=lambda persona: persona[1])

print(f"Personas ordenadas por edad: {ordenadas_por_edad}")

# Ejemplo 6: Usar lambdas como argumentos en funciones personalizadas
def aplicar_operacion(a: int, b: int, operacion: callable) -> int:
    """
    Aplica una operación definida por el usuario a dos números.
    Parámetros:
        a (int): Primer número.
        b (int): Segundo número.
        operacion (callable): Función que define la operación a realizar.
    Retorno:
        int: Resultado de la operación.
    """
    return operacion(a, b)

# Usar la función con una lambda
resultado_multiplicacion = aplicar_operacion(6, 7, lambda x, y: x * y)
print(f"El producto de 6 y 7 es: {resultado_multiplicacion}")

# Fin del archivo
