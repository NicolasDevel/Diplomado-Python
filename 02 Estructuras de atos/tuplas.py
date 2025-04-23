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
