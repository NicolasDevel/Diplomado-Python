"""
Un conjunto es una estructura de datos en Python que nos permite almacenar elementos únicos y desordenados.

Los conjuntos son útiles cuando necesitamos trabajar con elementos sin duplicados o
realizar operaciones matemáticas como uniones, intersecciones y diferencias.

Características principales:
- No permiten duplicados: Si intentas agregar un elemento repetido, el conjunto lo ignorará.
- No tienen un orden definido: Los elementos no están indexados, por lo que no
puedes acceder a ellos mediante índices.
- Son mutables: Puedes agregar o eliminar elementos después de crearlos.
"""

# Crear un conjunto vacío
conjunto_vacio = set()

# Crear un conjunto con valores
dias = {"Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}
print(dias)

# Los conjuntos no permiten duplicados
repetidos = {"Lunes", "Lunes", "Martes", "Martes"}
print(repetidos)  # Imprime {'Lunes', 'Martes'}

# Agregar elementos a un conjunto
dias.add("Sábado")
print(dias)

# Intentar agregar un elemento duplicado (no genera error, pero no lo agrega)
dias.add("Lunes")
print(dias)

# Eliminar elementos
dias.remove("Lunes")  # Si el elemento no existe, lanza un error
print(dias)

# Eliminar un elemento sin riesgo de error
dias.discard("Domingo")  # No lanza error si el elemento no está
print(dias)

# Obtener el tamaño de un conjunto
print(len(dias))

# Verificar si un elemento está en un conjunto
print("Martes" in dias)  # Devuelve True
print("Domingo" in dias)  # Devuelve False

# Uniones, intersecciones y diferencias
# Crear otro conjunto
fin_de_semana = {"Sábado", "Domingo"}

# Unión: Combina todos los elementos de ambos conjuntos
todos_los_dias = dias.union(fin_de_semana)
print("Unión:", todos_los_dias)

# Intersección: Obtiene los elementos comunes entre ambos conjuntos
dias_comunes = dias.intersection(fin_de_semana)
print("Intersección:", dias_comunes)

# Diferencia: Obtiene los elementos que están en 'dias' pero no en 'fin_de_semana'
dias_unicos = dias.difference(fin_de_semana)
print("Diferencia:", dias_unicos)

# Diferencia simétrica: Obtiene los elementos que están en un conjunto o en el otro, pero no en ambos
dias_diferentes = dias.symmetric_difference(fin_de_semana)
print("Diferencia simétrica:", dias_diferentes)

# Convertir una lista con duplicados a un conjunto para eliminar los duplicados
lista_con_duplicados = ["Lunes", "Martes", "Lunes", "Miércoles", "Martes"]
sin_duplicados = set(lista_con_duplicados)
print(sin_duplicados)

# Vaciar un conjunto
dias.clear()
print(dias)  # Conjunto vacío

# Copiar un conjunto
dias_copiados = fin_de_semana.copy()
print(dias_copiados)
