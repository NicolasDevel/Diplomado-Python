"""
    Los bucles son estructuras de control que permiten ejecutar un bloque de código
    de manera repetida. En Python, los dos bucles más utilizados son el bucle `for`
    y el bucle `while`. Ambos sirven para repetir acciones, pero se usan en diferentes situaciones.
"""


'''FOR'''

"""
    El bucle `for` en Python se usa para iterar sobre una secuencia
    (como una lista, tupla, cadena de texto, o incluso un rango de números).
    Es ideal cuando sabes cuántas veces necesitas ejecutar el bloque de código.
"""
for i in range(5):  # Itera desde 0 hasta 4
    print(i)

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)


"""
    El bloque else en un bucle for se ejecuta cuando el bucle termina su ejecución
    sin ser interrumpido por una declaración break.
"""
for i in range(5):
    print(i)
else:
    print("Bucle completo")



'''WHILE'''

"""
    El bucle while ejecuta un bloque de código de manera repetida mientras
    se cumpla una condición. Es útil cuando no sabes cuántas veces se debe
    ejecutar el bucle, sino que depende de una condición.
"""

condicion = True
while condicion:
    condicion = False
    # Código que se ejecuta mientras la condición sea True

i = 0
while i < 5:
    print(i)
    i += 1

"""
    El bloque else en un bucle while se ejecuta cuando el bucle
    termina su ejecución sin ser interrumpido por una declaración break.
"""


'''BREAK'''
"""
    La declaración break se usa para salir inmediatamente de un bucle,
    sin importar si la condición se sigue cumpliendo.
"""

for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i es igual a 5
    print(i)

'''COTINUE'''
"""
    La declaración continue se utiliza para saltar la iteración actual y
    continuar con la siguiente iteración del bucle.
"""

for i in range(5):
    if i == 3:
        continue  # Salta cuando i es igual a 3
    print(i)
