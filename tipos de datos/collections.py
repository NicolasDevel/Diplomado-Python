'''Listas'''

'''
    Cuando hablamos de una lista, nos referimos a una estructura de datos que nos permite almacenar varios
    elementos.
    Estos elementos pueden ser de diferentes tipos o incluso contener otras estructuras de datos.

    Las listas son ordenadas, ya que están organizadas por índices en forma ascendente.
    Son mutables, lo que significa que se puede manipular su tamaño, a diferencia de otros lenguajes
    donde la asignación de una lista (array) está limitada por el tamaño inicial.
'''

# Definir una lista vacía
lista = []

# Definir una lista con valores
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(semana)

# Acceder a un elemento a través de un índice
# Cada elemento de la lista está asociado a un índice
print(semana[0])  # Primer elemento
print(semana[2])  # Tercer elemento
print(semana[5])  # Sexto elemento
print(semana[-1])  # Último elemento usando índices negativos

# Obtener sublistas: Python nos ofrece una forma muy conveniente
dias_habiles = semana[0:5]  # Índices del 0 al 4
dias_habiles = semana[:5]  # Es equivalente a lo anterior
print(dias_habiles)

fin_de_semana = semana[5:]  # Desde el índice 5 hasta el final
print(fin_de_semana)

cada_dos_dias = semana[::2]  # Saltando de dos en dos
print(cada_dos_dias)

# Las listas son mutables: podemos agregar elementos
# La función append agrega un elemento al final de la lista
semana.append("Juernes")
print(semana)

# Cambiar un elemento de la lista
semana[-1] = "Día después del domingo"
print(semana)

# Insertar un elemento en un índice específico
semana.insert(4, "Juernes")
print(semana)

# Eliminar un elemento de dos formas: por índice o por valor
# Eliminar por índice
semana.pop(-1)  # Elimina el último elemento
print(semana)

# Eliminar un valor específico
semana.remove("Juernes")  # Elimina la primera coincidencia del valor
print(semana)

# Obtener el tamaño de una lista
tamano = len(semana)
print(tamano)

# Organizar listas
semana.sort()  # Orden ascendente
print("De forma ascendente:", semana)

semana.sort(reverse=True)  # Orden descendente
print("De forma descendente:", semana)

# Si quiero organizarla sin afectar la lista original
semana_ordenada = sorted(semana)

# Revertir una lista
semana.reverse()
print(semana)

# Verificar si un elemento existe en la lista
print("Lunes" in semana)  # Devuelve True

# Obtener el índice de un elemento
print("Donde esta índice de Lunes: ",semana.index("Lunes"))  # Devuelve 0

# Contar cuántas veces aparece un elemento
print(semana.count("Lunes"))

#Concatenar o unir listas
semestre_uno = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
semestro_dos = ["Julio", "Agosto", "Septiempre", "Octubre", "Noviembre", "Diciembre"]

print(semestre_uno + semestro_dos)


'''Tuplas'''

'''
    Una tupla es una estructura de datos en Python que nos permite almacenar varios elementos.

    A diferencia de las listas, las tuplas son inmutables, lo que significa que no pueden
    ser modificadas después de ser creadas. Esto las hace ideales para representar datos
    que no deberían cambiar durante la ejecución de un programa.

    Al igual que las listas, las tuplas son ordenadas, lo que significa que los elementos
    están organizados por índices en forma ascendente.

'''

print("TUPLAS")

# Definir una tupla vacía
tupla_vacia = ()

# Definir una tupla con valores
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(dias)

# Acceder a los elementos de una tupla
# Esto se hace de forma similar a las listas, usando índices
print(dias[0])  # Primer elemento
print(dias[2])  # Tercer elemento
print(dias[-1])  # Último elemento usando índices negativos

# Obtener subtuplas
# Esto funciona igual que las listas, pero el resultado será una nueva tupla
dias_habiles = dias[:5]  # Índices del 0 al 4
print(dias_habiles)

fin_de_semana = dias[5:]  # Desde el índice 5 hasta el final
print(fin_de_semana)

# Contar elementos en una tupla
print(len(dias))  # Tamaño de la tupla

# Verificar si un elemento existe en una tupla
print("Lunes" in dias)  # Devuelve True
print("Juernes" in dias)  # Devuelve False

# Obtener el índice de un elemento
print(dias.index("Miércoles"))  # Devuelve 2

# Contar cuántas veces aparece un elemento
print(dias.count("Lunes"))  # Devuelve 1

# Concatenar tuplas
tupla_extra = ("Juernes",)
dias_actualizados = dias + tupla_extra
print(dias_actualizados)

# Repetir tuplas
repetidos = dias * 2
print(repetidos)

# Desempaquetar tuplas
lunes, martes, miercoles, jueves, viernes, sabado, domingo = dias
print(lunes, martes, domingo)

# Las tuplas pueden almacenar diferentes tipos de datos
mi_tupla = (1, "Hola", True, [1, 2, 3])
print(mi_tupla)

# Aunque las tuplas son inmutables, si contienen elementos mutables como listas, esas listas sí pueden modificarse
mi_tupla[3].append(4)
print(mi_tupla)


"""Conjuntos (set)"""

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


"""Diccionarios"""

"""
Un diccionario es una estructura de datos en Python que almacena pares de clave-valor.
Cada clave debe ser única e inmutable (por ejemplo, cadenas, números o tuplas),
mientras que los valores pueden ser de cualquier tipo y repetirse.

Características principales:
- Almacenan datos en pares clave-valor.
- Son mutables: puedes agregar, modificar o eliminar elementos.
- Las claves no pueden repetirse, pero los valores sí.
- El orden de los elementos se mantiene desde Python 3.7.

"""

# Crear un diccionario vacío
diccionario_vacio = {}

# Crear un diccionario con valores
persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero",
    "ciudad": "Bogotá"
}
print(persona)

# Acceder a un valor por su clave
print(persona["nombre"])  # Imprime "Juan"

# Usar el método get para evitar errores si la clave no existe
print(persona.get("pais", "Clave no encontrada"))  # Imprime "Clave no encontrada"

# Agregar una nueva clave-valor
persona["pais"] = "Colombia"
print(persona)

# Modificar un valor existente
persona["edad"] = 31
print(persona)

# Eliminar un elemento por su clave
del persona["ciudad"]
print(persona)

# Otra forma de eliminar con el método pop (devuelve el valor eliminado)
profesion = persona.pop("profesion")
print("Profesión eliminada:", profesion)
print(persona)

# Verificar si una clave existe
print("edad" in persona)  # Devuelve True
print("ciudad" in persona)  # Devuelve False

# Obtener todas las claves, valores y pares clave-valor
print(persona.keys())   # Devuelve las claves
print(persona.values()) # Devuelve los valores
print(persona.items())  # Devuelve pares clave-valor como tuplas

# Recorrer un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Combinar dos diccionarios
otro_diccionario = {"hobby": "Música", "edad": 32}
persona.update(otro_diccionario)
print(persona)  # La clave "edad" será actualizada

# Crear un diccionario a partir de una lista de claves
nuevas_claves = ["clave1", "clave2", "clave3"]
valores_por_defecto = 0
nuevo_diccionario = dict.fromkeys(nuevas_claves, valores_por_defecto)
print(nuevo_diccionario)

# Copiar un diccionario
copia_persona = persona.copy()
print(copia_persona)

# Vaciar un diccionario
persona.clear()
print(persona)  # Diccionario vacío
