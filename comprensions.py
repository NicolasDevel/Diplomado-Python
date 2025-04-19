"""
    Las comprensiones permiten crear colecciones (listas, conjuntos, diccionarios) a
    partir de expresiones de manera más compacta. Por lo general,
    se usan para transformar o filtrar elementos de una secuencia (como una lista, tupla o cualquier iterable).
"""

# [expresión for elemento in iterable if condición]

# Crear una lista con los cuadrados de los números del 0 al 4

numeros = [1,2,3,4]
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)
print(cuadrados)  # [0, 1, 4, 9, 16]

cuadrados = [x**2 for x in numeros]
print(cuadrados)  # [0, 1, 4, 9, 16]

# Crear una lista con los cuadrados de los números impares del 0 al 9
numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados_impares = [x**2 for x in numeros if x % 2 != 0]
print(cuadrados_impares)  # [1, 9, 25, 49, 81]


import time

# Usando loop tradicional
start = time.time()
result1 = []
for i in range(1000000):
    result1.append(i * 2)
print("Tiempo con loop:", time.time() - start)

# Usando list comprehension
start = time.time()
result2 = [i * 2 for i in range(1000000)]
print("Tiempo con comprehension:", time.time() - start)


"""
Aunque las comprensiones son poderosas, su uso excesivo o con expresiones
demasiado complejas puede afectar la legibilidad del código.
Algunas recomendaciones:

Usar comprensiones simples: Mantén las expresiones fáciles de entender.

Evitar comprensiones anidadas complejas: Si la lógica dentro de la comprensión
es demasiado complicada, considera usar un bucle tradicional.

Usar condiciones claras: Si agregas una condición en una comprensión,
asegúrate de que sea fácil de entender a simple vista.
"""
