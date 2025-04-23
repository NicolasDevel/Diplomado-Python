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
